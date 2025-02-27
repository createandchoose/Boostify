import { createRouter, createWebHistory } from 'vue-router'
import MainLayout from '../components/MainLayout.vue'
import TasksView from '../components/TasksView.vue'
import CreateTaskView from '../components/CreateTaskView.vue'
import PanelView from '../components/PanelView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: MainLayout,
      children: [
        {
          path: '',
          redirect: '/tasks'
        },
        {
          path: '/tasks',
          name: 'tasks',
          component: TasksView
        },
        {
          path: '/create',
          name: 'create',
          component: CreateTaskView
        },
        {
          path: '/panel',
          name: 'panel',
          component: PanelView
        }
      ]
    }
  ]
})

export default router