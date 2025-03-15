<template>
  <div>
    <h1>Stock Data</h1>
    <p v-if="error">Error: {{ error }}</p>
    <p v-else-if="!open.length">Loading...</p>
    <p v-else>Latest Date: {{ data1?.[0]?.record_date }}</p>
    <v-chart v-else :option="chartOption" class="chart" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import VChart from 'vue-echarts';
import { use } from 'echarts/core';
import { TitleComponent, TooltipComponent, GridComponent, } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import { LineChart } from 'echarts/charts';

use([
  TitleComponent,
  TooltipComponent,
  GridComponent,
  CanvasRenderer,
  LineChart,
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
      labels.value.push(stock_data.value[i].record_date);
    }

    chartOption.value = {
  title: { text: 'Apple Stock Prices' },
  tooltip: { trigger: 'axis' },
  xAxis: { type: 'category', data: labels.value },
  yAxis: {
    type: 'value',
    min: 100,
    max: 300,
    interval: 50,
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
.chart {
  width: 1000px;
  height: 500px;
}

</style>
