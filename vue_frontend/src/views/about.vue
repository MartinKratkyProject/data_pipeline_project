<template>
    <section class="about-container">
      <el-card class="about-card" shadow="hover">
        <h1 class="about-title">About This Project</h1>
  
        <p>
          This application provides interactive and historical stock data visualization for major tech companies.
          It is built to be fast, modular, and robust — ideal for users who want both performance and clarity when analyzing stock movements.
        </p>
  
        <h2 class="section-title">Architecture Overview</h2>
        <p>
          The system operates in a containerized environment using <strong>Docker</strong>. Data collection and transformation are handled through <strong>Apache Airflow</strong> DAGs, which run daily at 7PM (Slovakia time) and fetch updated stock data from the <strong>Polygon API</strong>.
          This data is processed and stored in a <strong>PostgreSQL</strong> database.
        </p>
        <p>
          A <strong>Flask</strong> backend then serves this data through RESTful APIs, which are consumed by a <strong>Vue 3</strong> frontend powered by <strong>Element Plus</strong> and <strong>vue-echarts</strong> for visualization.
        </p>
  
        <h2 class="section-title">Technology Breakdown</h2>
  
        <h3 class="tech-subtitle">Docker</h3>
        <p>
          Docker is used to containerize all components of the system — from the data pipeline to the backend and frontend — ensuring consistency, isolation, and ease of deployment across environments.
        </p>
  
        <h3 class="tech-subtitle">Apache Airflow</h3>
        <p>
          Airflow orchestrates the daily ETL process. Its DAGs schedule and manage tasks such as fetching data from the Polygon API, transforming it, and storing it in the database. Airflow provides monitoring and logging for all stages of the pipeline.
        </p>
  
        <h3 class="tech-subtitle">Polygon API</h3>
        <p>
          Polygon provides real-time and historical financial data, which is critical for the accuracy and relevance of this application. Data includes stock prices, volume, and related metrics.
        </p>
  
        <h3 class="tech-subtitle">PostgreSQL</h3>
        <p>
          PostgreSQL serves as the relational database where all processed stock data is stored. It enables structured queries and efficient access for API endpoints.
        </p>
  
        <h3 class="tech-subtitle">Flask</h3>
        <p>
          Flask is used to build the backend API service. It handles incoming requests from the frontend, queries the database, and returns JSON responses with stock data.
        </p>
  
        <h3 class="tech-subtitle">Vue 3</h3>
        <p>
          The frontend is built using Vue 3, a progressive JavaScript framework that supports reactive, component-based development. It offers a performant and scalable UI foundation.
        </p>
  
        <h3 class="tech-subtitle">Element Plus</h3>
        <p>
          Element Plus provides Vue-compatible UI components, such as dropdowns, cards, and icons, to keep the interface polished and responsive without reinventing the wheel.
        </p>
  
        <h3 class="tech-subtitle">vue-echarts</h3>
        <p>
          For rich, interactive charts, vue-echarts is used. It offers deep integration with ECharts and allows the application to visualize time series stock data effectively.
        </p>
  
        <p class="thanks-text">Crafted with a modern stack and an eye on automation, data, and usability. Thank you for visiting.</p>
      </el-card>
    </section>
  </template>
  
  <script setup lang="ts">
  </script>
  
  <style scoped>
  .about-container {
    display: flex;
    justify-content: center;
    padding: 2em;
    background-color: #121212;
    min-height: 100vh;
  }
  
  .about-card {
    max-width: 900px;
    width: 100%;
    padding: 2em;
    background-color: #1e1e2f;
    border-radius: 12px;
    color: #e0e0e0;
  }
  
  .about-title {
    font-size: 2em;
    color: #c0aaff;
    margin-bottom: 1em;
  }
  
  .section-title {
    font-size: 1.5em;
    color: #a6a6d1;
    margin-top: 2em;
    margin-bottom: 0.5em;
  }
  
  .tech-subtitle {
    margin-top: 1.5em;
    font-size: 1.2em;
    color: #bb86fc;
  }
  
  p {
    margin-bottom: 1em;
    line-height: 1.6;
  }
  
  a {
    color: #9ab8ff;
    text-decoration: none;
    font-weight: bold;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  .thanks-text {
    margin-top: 3em;
    font-style: italic;
    color: #888;
  }
  </style>
  