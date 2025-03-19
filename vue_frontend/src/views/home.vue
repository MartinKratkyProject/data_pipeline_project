<template>
  <div class="container">
    <h1>Stock Dashboard</h1>
    <p class="timestamp">Current Time: {{ currentTime }}</p>
    
    <!-- Stock Summary -->
    <div class="stock-summary">
      <div class="summary-card" v-for="(stock, ticker) in stockData" :key="ticker">
        <h3>{{ ticker.toUpperCase() }}</h3>
        <p>Open: {{ stock.open }}</p>
        <p>High: {{ stock.high }}</p>
        <p>Low: {{ stock.low }}</p>
        <p>Close: {{ stock.close }}</p>
        <p>Volume: {{ stock.volume }}</p>
      </div>
    </div>

    <!-- Transactions Table -->
    <div class="table-container">
      <h2>Recent Transactions</h2>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Ticker</th>
            <th>Open</th>
            <th>High</th>
            <th>Low</th>
            <th>Close</th>
            <th>Volume</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in transactions" :key="index">
            <td>{{ item.date }}</td>
            <td>{{ item.ticker.toUpperCase() }}</td>
            <td>{{ item.open }}</td>
            <td>{{ item.high }}</td>
            <td>{{ item.low }}</td>
            <td>{{ item.close }}</td>
            <td>{{ item.volume }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// Dummy stock data for multiple tickers
const stockData = ref({
  apple: { open: 224.5, high: 225.69, low: 221.33, close: 221.69, volume: 37595470 },
  amazon: { open: 171.09, high: 174.21, low: 170.97, close: 173.66, volume: 53006286 },
  google: { open: 244.33, high: 244.98, low: 239.13, close: 240.36, volume: 40678483 },
  nvidia: { open: 315.45, high: 320.78, low: 310.12, close: 318.67, volume: 48231784 },
  tesla: { open: 189.55, high: 192.10, low: 185.90, close: 190.22, volume: 67341258 }
});

// Dummy transaction data for multiple tickers
const transactions = ref([
  { date: "2024-10-07", ticker: "apple", open: 224.5, high: 225.69, low: 221.33, close: 221.69, volume: 37595470 },
  { date: "2023-10-04", ticker: "amazon", open: 171.09, high: 174.21, low: 170.97, close: 173.66, volume: 53006286 },
  { date: "2025-02-26", ticker: "google", open: 244.33, high: 244.98, low: 239.13, close: 240.36, volume: 40678483 },
  { date: "2025-01-15", ticker: "nvidia", open: 315.45, high: 320.78, low: 310.12, close: 318.67, volume: 48231784 },
  { date: "2024-11-30", ticker: "tesla", open: 189.55, high: 192.10, low: 185.90, close: 190.22, volume: 67341258 }
]);

// Real-time clock
const currentTime = ref(new Date().toLocaleTimeString());

onMounted(() => {
  setInterval(() => {
    currentTime.value = new Date().toLocaleTimeString();
  }, 1000);
});
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: auto;
  padding: 20px;
}

h1, h2 {
  text-align: center;
  color: #333;
}

.timestamp {
  text-align: center;
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 20px;
}

.stock-summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
  margin-bottom: 20px;
}

.summary-card {
  background: #1f068f;
  padding: 15px;
  text-align: center;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}

.table-container {
  margin-top: 20px;
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

th {
  background: #42b983;
  color: white;
}
</style>
