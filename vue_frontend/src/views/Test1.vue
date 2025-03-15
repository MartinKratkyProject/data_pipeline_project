<template>
  <div>
    <h1>Stock Data</h1>
    <p v-if="error">Error: {{ error }}</p>
    <p v-else-if="!open.length">Loading...</p>
    <p v-else>Latest Date: {{ data1?.[0]?.record_date }}</p>
    <v-chart v-else :option="chartOption" style="width: 600px; height: 400px" />
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
const labels = ref([]);
const data1 = ref([]);
const error = ref(null);

const chartOption = ref({
  title: { text: 'Stock Opening Prices' },
  tooltip: { trigger: 'axis' },
  xAxis: {
    type: 'category',
    data: labels.value,
  },
  yAxis: {
    type: 'value',
  },
  series: [
    {
      name: 'Open Price',
      data: open.value,
      type: 'line',
      smooth: true,
    },
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
    labels.value = [];

    for (let i = 0; i < data1.value.length; i++) {
      open.value.push(data1.value[i].open);
      labels.value.push(data1.value[i].record_date);
    }
    
  } catch (err) {
    error.value = err.message;
  }
};

watch(open, () => {
  chartOption.value = {
    ...chartOption.value,
    xAxis: { type: 'category', data: labels.value },
    series: [{ name: 'Open Price', data: open.value, type: 'line', smooth: true }],
  };
});

onMounted(fetchData);
</script>
