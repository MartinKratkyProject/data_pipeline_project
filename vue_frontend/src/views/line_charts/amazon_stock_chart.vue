<template>
  <div class="app-container">
    <div class="header">
      <h1>Amazon Stock Tracker</h1>
      <p>Daily open, close, high, and low prices visualized</p>
      <p class="timestamp">{{ currentDate }} | {{ currentTime }}</p>
      <p class="record-date">Latest Stock Data: {{ formattedRecordDate }}</p>
    </div>

    <div v-if="error" class="error">Error: {{ error }}</div>
    <div v-else-if="!open.length" class="loading">Loading...</div>
    
    <div v-else class="chart-wrapper">
      <div class="stats-card">
        <p><strong>Open:</strong> {{ latest.open }}</p>
        <p><strong>Close:</strong> {{ latest.close }}</p>
        <p><strong>High:</strong> {{ latest.high }}</p>
        <p><strong>Low:</strong> {{ latest.low }}</p>
      </div>

      <v-chart :option="chartOption" class="chart" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import VChart from 'vue-echarts';
import { use } from 'echarts/core';
import { TitleComponent, TooltipComponent, GridComponent, LegendComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import { LineChart } from 'echarts/charts';

use([TitleComponent, TooltipComponent, GridComponent, CanvasRenderer, LineChart, LegendComponent]);

const open = ref([]);
const close = ref([]);
const high = ref([]);
const low = ref([]);
const labels = ref([]);
const stock_data = ref([]);
const error = ref(null);
const chartOption = ref({});

const latest = computed(() => stock_data.value[stock_data.value.length - 1] || {});

// Time/date logic
const currentTime = ref(new Date().toLocaleTimeString());
const currentDate = ref(
  new Date().toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
);

const formattedRecordDate = computed(() => {
  if (!stock_data.value.length) return 'No data available';
  const rawDate = stock_data.value[stock_data.value.length - 1].record_date;
  const dateObj = new Date(rawDate);
  return dateObj.toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
});

onMounted(() => {
  fetchData();
  setInterval(() => {
    currentTime.value = new Date().toLocaleTimeString();
  }, 1000);
});

const fetchData = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/amzn');
    if (!response.ok) throw new Error('Failed to fetch data');
    
    stock_data.value = await response.json();
    stock_data.value.sort((a, b) => new Date(a.record_date) - new Date(b.record_date));

    open.value = stock_data.value.map(s => s.open);
    close.value = stock_data.value.map(s => s.close);
    high.value = stock_data.value.map(s => s.high);
    low.value = stock_data.value.map(s => s.low);
    labels.value = stock_data.value.map(s => new Date(s.record_date).toISOString().split('T')[0]);

    chartOption.value = {
      backgroundColor: '#242424',
      textStyle: {
        color: '#f5f5f5'
      },
      title: {
        text: 'Amazon Stock Prices',
        left: 'center',
        textStyle: {
          color: '#ffffff'
        }
      },
      tooltip: {
        trigger: 'axis',
        backgroundColor: '#333',
        borderColor: '#888',
        textStyle: {
          color: '#ffffff'
        }
      },
      legend: {
        bottom: 0,
        left: 'center',
        textStyle: {
          color: '#f0f0f0'
        }
      },
      xAxis: {
        type: 'category',
        data: labels.value,
        axisLine: { lineStyle: { color: '#888' } },
        axisLabel: { color: '#f0f0f0' }
      },
      yAxis: {
        type: 'value',
        min: Math.floor(Math.min(...low.value) / 100) * 100,
        max: Math.ceil(Math.max(...high.value) / 100) * 100,
        axisLine: { lineStyle: { color: '#888' } },
        axisLabel: { color: '#f0f0f0' },
        splitLine: {
          lineStyle: {
            color: '#444'
          }
        }
      },
      series: [
        {
          name: 'Open Price',
          data: open.value,
          type: 'line',
          smooth: true,
        },
        {
          name: 'Close Price',
          data: close.value,
          type: 'line',
          smooth: true,
        },
        {
          name: 'High Price',
          data: high.value,
          type: 'line',
          smooth: true,
        },
        {
          name: 'Low Price',
          data: low.value,
          type: 'line',
          smooth: true,
        },
      ],
    };

  } catch (err) {
    error.value = err.message;
  }
};
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  font-family: 'Segoe UI', sans-serif;
  background: #181818;
  color: #f0f0f0;
  min-height: 100vh;
}

.header {
  text-align: center;
  margin-bottom: 2rem;
}

.header h1 {
  color: #ffffff;
}

.header p {
  color: #cccccc;
  margin: 0.3rem 0;
}

.timestamp,
.record-date {
  font-size: 1.1rem;
  color: #a4b0be;
  margin-bottom: 0.5rem;
}

.chart-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #242424;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
  padding: 2rem;
  width: 100%;
  max-width: 1100px;
}

.chart {
  width: 100%;
  height: 500px;
  margin-top: 1.5rem;
}

.stats-card {
  background: #2a2a2a;
  border-radius: 12px;
  padding: 1rem 2rem;
  margin-bottom: 1rem;
  text-align: left;
  width: 100%;
  color: #f5f5f5;
  box-shadow: inset 0 0 5px rgba(255, 255, 255, 0.05);
}

.stats-card h2 {
  color: #ffffff;
}

.stats-card p {
  margin: 0.2rem 0;
  color: #dddddd;
}

.loading {
  font-size: 1.2rem;
  font-weight: bold;
  color: #bbbbbb;
}

.error {
  color: #ff6b6b;
  font-weight: bold;
  margin: 2rem;
}
</style>
