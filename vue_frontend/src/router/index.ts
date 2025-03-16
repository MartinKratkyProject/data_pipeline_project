import { createRouter, createWebHistory } from 'vue-router'
import Test1 from '../views/line_charts/apple_stock_chart.vue'
import test_design from '../views/test_design.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/test',
      name: 'test',
      component: test_design,
    },
  ],
})

export default router
