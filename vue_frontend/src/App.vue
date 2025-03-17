<template>
  <div>
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li>
          <el-dropdown trigger="click" hide-on-click="false">
            <span class="dropdown-trigger">
              Tickers
              <el-icon><ArrowDown /></el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>
                  <router-link to="/tickers/option1">Option 1</router-link>
                </el-dropdown-item>
                <el-dropdown-item>
                  <router-link to="/tickers/option2">Option 2</router-link>
                </el-dropdown-item>
                <el-dropdown-item>
                  <router-link to="/tickers/option3">Option 3</router-link>
                </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </li>
        <li><router-link to="/test">Powered by</router-link></li>
        <li><router-link to="/">About</router-link></li>
      </ul>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script setup lang="ts">
import { ArrowDown } from "@element-plus/icons-vue";
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
  align-items: center; /* Fixes alignment issue */
  justify-content: center;
  gap: 1.5em;
  padding: 0;
  margin: 0;
}

li {
  font-size: 18px;
}

nav a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  padding: 10px 16px;
  border-radius: 8px;
  transition: background 0.2s ease-in-out, transform 0.2s;
}

nav a:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

.dropdown-trigger {
  color: white;
  font-weight: bold;
  font-size: 18px;
  padding: 10px 16px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  cursor: pointer;
  gap: 5px;
  transition: background 0.2s ease-in-out, transform 0.2s;
}

.dropdown-trigger:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

.el-dropdown-menu {
  background-color: white;
  color: black;
}
</style>
