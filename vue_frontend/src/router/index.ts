import { createRouter, createWebHistory } from 'vue-router'
import Test1 from '../views/line_charts/apple_stock_chart.vue'

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
