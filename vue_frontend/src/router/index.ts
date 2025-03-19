import { createRouter, createWebHistory } from 'vue-router'
import apple from '../views/line_charts/apple_stock_chart.vue'
import amazon from '../views/line_charts/amazon_stock_chart.vue'
import google from '../views/line_charts/google_stock_chart.vue'
import nvidia from '../views/line_charts/nvidia_stock_chart.vue'
import tesla from '../views/line_charts/tesla_stock_chart.vue'
import about from '../views/about.vue'
import home from '../views/home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/apple',
      name: 'apple',
      component: apple,
    },
    {
      path: '/amazon',
      name: 'amazon',
      component: amazon,
    },
    {
      path: '/google',
      name: 'google',
      component: google,
    },
    {
      path: '/nvidia',
      name: 'nvidia',
      component: nvidia,
    },
    {
      path: '/tesla',
      name: 'tesla',
      component: tesla,
    },
    {
      path: '/about',
      name: 'about',
      component: about,
    },
    {
      path: '/',
      name: 'home',
      component: home,
    },
  ],
})

export default router
