<template>
  <div>
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li>
          <el-dropdown>
            <span class="dropdown-trigger">Tickers</span>
            <template #dropdown>
              <el-dropdown-menu>
                <router-link to="/tickers/option1">Apple</router-link>
                <router-link to="/tickers/option2">Amazon</router-link>
                <router-link to="/tickers/option3">Google</router-link>
                <router-link to="/tickers/option2">Nvidia</router-link>
                <router-link to="/tickers/option3">Tesla</router-link>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </li>
        <li>
          <el-dropdown>
            <span class="dropdown-trigger">Powered by</span>
            <template #dropdown>
              <el-dropdown-menu>
                <router-link to="/tickers/option1">Vue3</router-link>
                <router-link to="/tickers/option2">Element Plus</router-link>
                <router-link to="/tickers/option3">Echarts</router-link>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </li>
        <li><router-link to="/">About</router-link></li>
      </ul>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script setup lang="ts">
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

li {
  font-size: 18px;
}

nav a {
  color: white;
  font-weight: bold;
  padding: 10px 16px;
  border-radius: 8px;
  transition: background 0.2s ease-in-out, transform 0.2s;
}

nav a:hover, 
.dropdown-trigger:hover,
.el-dropdown-menu a:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

nav a, 
.dropdown-trigger,
.el-dropdown-menu a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  padding: 10px 16px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: background 0.2s ease-in-out, transform 0.2s;
}

.el-dropdown-menu {
  background-color: rgb(111, 118, 218);
  color: black;
  display: flex;
  flex-direction: column;
  padding: 5px;
}

.el-dropdown-menu .el-dropdown-item, 
.el-dropdown-menu a {
  display: block;
  padding: 8px 12px;
  text-align: left;
  color: white;
}

</style>
