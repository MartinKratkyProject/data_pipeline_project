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
import { ref, onMounted, watch } from 'vue';
import VChart from 'vue-echarts';
import { use } from 'echarts/core';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DatasetComponent,
  ToolboxComponent,
} from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import { BarChart, LineChart } from 'echarts/charts';

use([
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DatasetComponent,
  ToolboxComponent,
  CanvasRenderer,
  BarChart,
  LineChart,
]);

const open = ref([]);
const close = ref([]);
const high = ref([]);
const low = ref([]);
const labels = ref([]);
const data1 = ref([]);
const error = ref(null);

const chartOption = ref({
  title: { text: 'Apple Stock Prices' },
  tooltip: { trigger: 'axis' },
  legend: {
    show: true,
    bottom: '5%', // Put legend at the bottom of the chart
    left: 'center', // Center the legend
    orient: 'horizontal', // Arrange items in a row
    textStyle: { color: '#000', fontSize: 14 }, // Text style
    backgroundColor: '#fff', // Optional, just for testing purposes
    borderWidth: 1, // Optional, just for testing purposes
  },
  grid: {
    top: '10%', // Keep some space on top for the title
    left: '10%',
    right: '10%',
    bottom: '15%', // Adjust bottom to make space for the legend
  },
  xAxis: {
    type: 'category',
    data: labels.value,
  },
  yAxis: {
    type: 'value',
  },
  series: [
    { name: 'Open Price', data: open.value, type: 'line', smooth: true },
    { name: 'Close Price', data: close.value, type: 'line', smooth: true },
    { name: 'High Price', data: high.value, type: 'line', smooth: true },
    { name: 'Low Price', data: low.value, type: 'line', smooth: true },
  ],
});

const fetchData = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/aapl');
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    
    data1.value = await response.json();

    // Sort data based on record_date
    data1.value.sort((a, b) => new Date(a.record_date) - new Date(b.record_date));

    open.value = [];
    close.value = [];
    high.value = [];
    low.value = [];
    labels.value = [];

    for (let i = 0; i < data1.value.length; i++) {
      open.value.push(data1.value[i].open);
      close.value.push(data1.value[i].close);
      high.value.push(data1.value[i].high);
      low.value.push(data1.value[i].low);
      labels.value.push(data1.value[i].record_date);
    }
    
  } catch (err) {
    error.value = err.message;
  }
};

watch([open, close, high, low], () => {
  chartOption.value = {
    title: { text: 'Apple Stock Prices' },
    tooltip: { trigger: 'axis' },
    xAxis: { type: 'category', data: labels.value },
    yAxis: { type: 'value' },
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
});


onMounted(fetchData);
</script>
<style>
.chart {
  width: 1000px;
  height: 600px;
  max-width: 100%;
}

</style>