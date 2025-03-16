<template>
  <div>
    <!-- Navbar: This will be visible on all pages -->
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/test">Test</router-link></li>
        <!-- Add more links as needed -->
      </ul>
    </nav>

    <!-- Route-specific content will be injected here -->
    <router-view></router-view>
  </div>
</template>

<script setup lang="ts">
// No need to import route-specific components here, as they are handled by the router
</script>

<style scoped>
/* Styling for your navbar */
nav {
  background-color: #e22525;
  color: white;
  padding: 1em;
}

ul {
  list-style-type: none;
  display: flex;
  gap: 1em;
}

li {
  font-size: 18px;
}

router-link {
  text-decoration: none;
  color: white;
}

router-link:hover {
  text-decoration: underline;
}
</style>
