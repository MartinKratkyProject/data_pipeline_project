<script setup>
import { ref, onMounted } from 'vue';

const data = ref(null);
const error = ref(null);

const fetchData = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/aapl');
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    data.value = await response.json();
  } catch (err) {
    error.value = err.message;
  }
};

onMounted(fetchData);
</script>

<template>
  <div>
    <h1>Stock Data</h1>
    <div v-if="error">Error: {{ error }}</div>
    <div v-else-if="!data">Loading...</div>
    <div v-else>
      <pre>{{ data[0] }}</pre>
    </div>
  </div>
</template>
