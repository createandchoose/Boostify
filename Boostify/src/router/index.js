import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Profile from '../views/Profile.vue'
import Shop from '../views/Shop.vue'
import Games from '../views/Games.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/shop',
      name: 'Shop',
      component: Shop
    },
    {
      path: '/games',
      name: 'Games',
      component: Games
    }
  ]
})

export default router