import { createRouter, createWebHistory } from 'vue-router'
import Test1 from '../views/Test1.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    {
      path: '/',
      name: 'home',
      component: Test1,
    },
  ],
})

export default router
