import { createRouter, createWebHistory } from 'vue-router'
import MainLayout from '../components/MainLayout.vue'
import HomeView from '../components/HomeView.vue'
import ProfileView from '../components/ProfileView.vue'
import LeaderboardView from '../components/LeaderboardView.vue'
import MarketView from '../components/MarketView.vue'
import TasksView from '../components/TasksView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: MainLayout,
      children: [
        {
          path: '',
          name: 'home',
          component: HomeView
        },
        {
          path: 'profile',
          name: 'profile',
          component: ProfileView
        },
        {
          path: 'leaderboard',
          name: 'leaderboard',
          component: LeaderboardView
        },
        {
          path: 'market',
          name: 'market',
          component: MarketView
        },
        {
          path: 'tasks',
          name: 'tasks',
          component: TasksView
        }
      ]
    }
  ]
})

export default router