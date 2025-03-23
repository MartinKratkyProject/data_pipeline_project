<template>
  <div class="container">
    <h1>Stock Dashboard</h1>
    <p class="timestamp">{{ currentDate }} | {{ currentTime }}</p>

    <div v-if="home_data.length">
      <p class="record-date">Latest Data: {{ formattedRecordDate }}</p>

      <table class="stock-table">
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Open</th>
            <th>Close</th>
            <th>Change (%)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in home_data" :key="item.ticker">
            <td>{{ item.ticker }}</td>
            <td>${{ item.open.toFixed(2) }}</td>
            <td>${{ item.close.toFixed(2) }}</td>
            <td :class="{ positive: item.close - item.open >= 0, negative: item.close - item.open < 0 }">
              {{ ((item.close - item.open) / item.open * 100).toFixed(2) }}%
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <p v-else class="loading">Loading stock data...</p>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';

const currentTime = ref(new Date().toLocaleTimeString());
const currentDate = ref(new Date().toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }));
const home_data = ref([]);

onMounted(() => {
  setInterval(() => {
    currentTime.value = new Date().toLocaleTimeString();
  }, 1000);

  fetchData();
});

const fetchData = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/home');
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    
    home_data.value = await response.json();
  } catch (error) {
    console.error(error);
  }
};

// Format the date of the latest record
const formattedRecordDate = computed(() => {
  if (home_data.value.length === 0) return "No data available";

  const rawDate = home_data.value[0].record_date; // Example: "2024-03-22"
  const dateObj = new Date(rawDate);
  
  return dateObj.toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
});
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  text-align: center;
}

h1 {
  color: #333;
}

.timestamp, .record-date {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 20px;
}

.stock-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.stock-table th, .stock-table td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: center;
}

.stock-table th {
  background-color: #2426a7;
  font-weight: bold;
}

.positive {
  color: green;
  font-weight: bold;
}

.negative {
  color: red;
  font-weight: bold;
}

.loading {
  font-size: 1.2rem;
  color: #999;
}
</style>
