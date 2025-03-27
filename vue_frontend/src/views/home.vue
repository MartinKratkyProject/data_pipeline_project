<template>
  <div class="container">
    <h1>Stock Dashboard</h1>
    <p class="timestamp">{{ currentDate }} | {{ currentTime }}</p>

    <div v-if="home_data.length">
      <p class="record-date">Latest Data: {{ formattedRecordDate }}</p>

      <div class="table-container">
        <table class="stock-table">
          <thead>
            <tr>
              <th>Ticker</th>
              <th>Daily Change (%)</th>
              <th>Weekly Change (%)</th>
              <th>Monthly Change (%)</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in home_data" :key="item.ticker">
              <td>{{ item.ticker }}</td>
              <td :class="getClass(item.dailyChange)">
                {{ item.dailyChange.toFixed(2) }}%
              </td>
              <td :class="getClass(item.weeklyChange)">
                {{ item.weeklyChange.toFixed(2) }}%
              </td>
              <td :class="getClass(item.monthlyChange)">
                {{ item.monthlyChange.toFixed(2) }}%
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <p v-else class="loading">Loading stock data...</p>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';

const currentTime = ref(new Date().toLocaleTimeString());
const currentDate = ref(
  new Date().toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
);
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
    
    const data = await response.json();
    home_data.value = data.map(item => ({
      ...item,
      dailyChange: calculatePercentageChange(item.open, item.close),
      weeklyChange: calculatePercentageChange(item.week_open, item.close),
      monthlyChange: calculatePercentageChange(item.month_open, item.close),
    }));
  } catch (error) {
    console.error(error);
  }
};

const calculatePercentageChange = (open, close) => {
  return open ? ((close - open) / open) * 100 : 0;
};

const getClass = (value) => {
  return value >= 0 ? 'positive' : 'negative';
};

const formattedRecordDate = computed(() => {
  if (home_data.value.length === 0) return "No data available";

  const rawDate = home_data.value[0].record_date;
  const dateObj = new Date(rawDate);
  
  return dateObj.toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
});
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: auto;
  padding: 20px;
  text-align: center;
  font-family: Arial, sans-serif;
  color: #ffffff;
}

h1 {
  color: #dcdde1;
  margin-bottom: 10px;
}

.timestamp, .record-date {
  font-size: 1.2rem;
  color: #a4b0be;
  margin-bottom: 20px;
}

.table-container {
  overflow-x: auto;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
}

.stock-table {
  width: 100%;
  border-collapse: collapse;
  background: #2f2f4f;
  border-radius: 10px;
  overflow: hidden;
}

.stock-table th, .stock-table td {
  padding: 12px;
  text-align: center;
  border-bottom: 1px solid #444;
}

.stock-table th {
  background-color: rgb(96, 65, 210);
  color: white;
  font-weight: bold;
}

.stock-table tr:nth-child(even) {
  background-color: #3a3a6d;
}

.stock-table tr:nth-child(odd) {
  background-color: #2f2f4f;
}

.stock-table tr:hover {
  background-color: #4b4b8f;
}

.positive {
  color: #2ecc71;
  font-weight: bold;
}

.negative {
  color: #e74c3c;
  font-weight: bold;
}

.loading {
  font-size: 1.2rem;
  color: #95a5a6;
}
</style>