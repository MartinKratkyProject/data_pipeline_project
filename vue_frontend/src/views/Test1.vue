<template>
  <div>
    <p v-if="error">Error: {{ error }}</p>
    <p v-else-if="!open.length">Loading...</p>
    <p v-else>Latest Date: {{ stock_data?.[0]?.record_date }}</p>
    <v-chart v-else :option="chartOption" class="chart" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import VChart from 'vue-echarts';
import { use } from 'echarts/core';
import { TitleComponent, TooltipComponent, GridComponent, LegendComponent, } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import { LineChart } from 'echarts/charts';

use([
  TitleComponent,
  TooltipComponent,
  GridComponent,
  CanvasRenderer,
  LineChart,
  LegendComponent,
]);

const open = ref([]);
const close = ref([]);
const high = ref([]);
const low = ref([]);
const labels = ref([]);
const stock_data = ref([]);
const error = ref(null);
const chartOption = ref({});

const fetchData = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/aapl');
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    
    stock_data.value = await response.json();
    stock_data.value.sort((a, b) => new Date(a.record_date) - new Date(b.record_date));

    open.value = [];
    close.value = [];
    high.value = [];
    low.value = [];
    labels.value = [];

    for (let i = 0; i < stock_data.value.length; i++) {
      open.value.push(stock_data.value[i].open);
      close.value.push(stock_data.value[i].close);
      high.value.push(stock_data.value[i].high);
      low.value.push(stock_data.value[i].low);
      
      labels.value.push(new Date(stock_data.value[i].record_date).toISOString().split('T')[0]);
    }

    chartOption.value = {
      title: { text: 'Apple Stock Prices', left: 'center' },
      tooltip: { trigger: 'axis' },
      legend: { 
        bottom: 0,  // Places the legend at the bottom
        left: 'center' 
      },
      xAxis: { type: 'category', data: labels.value },
      yAxis: {
        type: 'value',
        min: Math.round(Math.min(...low.value) / 100) * 100,
        max: Math.round(Math.max(...high.value) / 100) * 100,
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

onMounted(fetchData);
</script>

<style>
.chart-container {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  width: 100%;
  height: 100vh;
}

.chart {
  width: 1000px;
  height: 500px;
}

</style>
