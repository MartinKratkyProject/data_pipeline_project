<template>
  <div>
    <nav>
      <ul>
        <li>
          <router-link to="/">
            Home
            <el-icon class="nav-icon"><HomeFilled /></el-icon>
          </router-link>
        </li>
        <li>
          <el-dropdown>
            <span class="dropdown-trigger">
              Tickers
              <el-icon class="nav-icon"><TrendCharts /></el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <router-link class="dropdown-link" to="/apple">Apple</router-link>
                <router-link class="dropdown-link" to="/amazon">Amazon</router-link>
                <router-link class="dropdown-link" to="/google">Google</router-link>
                <router-link class="dropdown-link" to="/nvidia">Nvidia</router-link>
                <router-link class="dropdown-link" to="/tesla">Tesla</router-link>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </li>
        <li>
          <el-dropdown>
            <span class="dropdown-trigger">Powered by <el-icon class="nav-icon"><Cpu /></el-icon></span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-menu-item><a class="dropdown-link" href="https://vite.dev/">Vite</a></el-dropdown-menu-item>
                <el-dropdown-menu-item><a class="dropdown-link" href="https://vuejs.org/">Vue3</a></el-dropdown-menu-item>
                <el-dropdown-menu-item><a class="dropdown-link" href="https://element-plus.org/en-US/">Element Plus</a></el-dropdown-menu-item>
                <el-dropdown-menu-item><a class="dropdown-link" href="https://vue-echarts.dev/">vue-echarts</a></el-dropdown-menu-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </li>
        <li><router-link to="/about">About<el-icon class="nav-icon"><InfoFilled /></el-icon></router-link></li>
      </ul>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script setup lang="ts">
import { HomeFilled, TrendCharts, Cpu, InfoFilled } from "@element-plus/icons-vue";
</script>

<style scoped>
nav {
  background-color: rgb(41, 15, 136);
  padding: 1em 2em;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

ul {
  list-style-type: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5em;
  padding: 0;
  margin: 0;
}

li, .dropdown-trigger {
  font-size: 20px;
}

nav a, .dropdown-trigger, .dropdown-link {
  color: white;
  font-weight: bold;
  padding: 10px 16px;
  border-radius: 8px;
  transition: background 0.2s ease-in-out, transform 0.2s;
  display: flex;
  align-items: center;
  text-decoration: none;
  cursor: pointer;
}

nav a:hover, 
.dropdown-trigger:hover,
.dropdown-link:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

.nav-icon {
  margin-left: 5px;
}

.el-dropdown-menu {
  background-color: rgb(111, 118, 218);
  display: flex;
  flex-direction: column;
  padding: 5px;
}

.dropdown-link {
  padding: 10px 16px;
}

</style>
