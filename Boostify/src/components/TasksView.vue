<template>
  <div class="min-h-screen bg-white">
    <div class="px-4 pt-4">
      <h1 class="text-2xl font-bold mb-4">Таски</h1>

      <!-- Tabs -->
      <div class="flex gap-2 mb-6">
        <button 
          v-for="tab in tabs" 
          :key="tab.id"
          @click="currentTab = tab.id"
          class="px-4 py-2 rounded-full text-sm"
          :class="currentTab === tab.id ? 'bg-gray-100 font-medium' : 'text-gray-500'"
        >
          {{ tab.name }}
        </button>
      </div>

      <!-- Tasks List -->
      <div v-if="currentTab === 'tasks'" class="space-y-6">
        <div v-for="task in tasks" :key="task.id" 
          class="bg-gray-50 rounded-xl p-4">
          <!-- Status Badge -->
          <div class="inline-block px-2 py-1 bg-gray-200 rounded-md text-xs text-gray-600 mb-3">
            {{ task.status }}
          </div>

          <h3 class="font-medium mb-2">{{ task.title }}</h3>
          <p class="text-sm text-gray-600 mb-4">{{ task.description }}</p>

          <!-- Rewards -->
          <div class="flex items-center gap-4 mb-3">
            <div class="flex items-center gap-1">
              <Star class="w-4 h-4 text-yellow-500" />
              <span class="text-sm">{{ task.rewards.points }} Баллов</span>
            </div>
            <div class="flex items-center gap-1">
              <CircleDollarSign class="w-4 h-4 text-gray-900" />
              <span class="text-sm">{{ task.rewards.boost }} BOOST</span>
            </div>
          </div>

          <!-- Deadline and Action -->
          <div class="flex items-center justify-between">
            <div class="text-sm text-gray-500">
              Сроки: {{ task.deadline }}
            </div>
            <button 
              class="flex items-center gap-2 px-4 py-2 bg-gray-100 rounded-lg text-sm text-gray-600"
              :class="{'bg-gray-100': task.status === 'В процессе', 'bg-yellow-100 text-yellow-700': task.status === 'На проверке'}"
            >
              <FileText class="w-4 h-4" />
              {{ task.status === 'В процессе' ? 'Отправить на проверку' : 'На проверке' }}
            </button>
          </div>
        </div>
      </div>

      <!-- Notifications Tab -->
      <div v-if="currentTab === 'notifications'" class="text-gray-500 text-center py-8">
        Нет новых уведомлений
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Star, CircleDollarSign, FileText } from 'lucide-vue-next'

const currentTab = ref('tasks')

const tabs = [
  { id: 'tasks', name: 'Задачи' },
  { id: 'notifications', name: 'Уведомления' }
]

const tasks = [
  {
    id: 1,
    status: 'В процессе',
    title: 'Сверхурочная работа',
    description: 'В случае возникновения срочных задач, требующих вашего внимания после окончания рабочего дня, проявите готовность остаться и завершить проект в срок. Ваше участие будет способствовать своевременному выполнению важных задач.',
    rewards: {
      points: 50,
      boost: 50
    },
    deadline: 'До 02.03.2025'
  },
  {
    id: 2,
    status: 'На проверке',
    title: 'Замещение отсутствующих коллег',
    description: 'В случае отсутствия ваших коллег по причине болезни или отпуска, принимайте на себя дополнительные функции, чтобы обеспечить бесперебойную работу отдела. Ваша гибкость и ответственность помогут нам справиться с любыми трудностями.',
    rewards: {
      points: 50,
      boost: 10
    },
    deadline: 'До 01.03.2025'
  }
]
</script>