<template>
  <div class="min-h-screen bg-white">
    <div class="px-4 py-4">
      <h1 class="text-xl font-bold mb-6">Панель рук.</h1>

      <!-- Profile -->
      <div class="flex items-center gap-3 mb-6">
        <div class="w-12 h-12 rounded-full bg-emerald-500 flex items-center justify-center">
          <User class="w-6 h-6 text-white" />
        </div>
        <div class="flex-1">
          <div class="flex items-center gap-2">
            <span class="font-medium">Айтал Попов</span>
            <span class="px-2 py-0.5 bg-gray-900 text-white rounded-full text-xs">
              Персонал
            </span>
          </div>
          <div class="text-sm text-gray-500">Руководитель</div>
        </div>
      </div>

      <!-- Leaderboard -->
      <div class="mb-4 flex items-center justify-between">
        <h2 class="font-medium">Таблица лидеров</h2>
        <span class="text-sm text-gray-400">Топ 10</span>
      </div>

      <div class="space-y-4">
        <div v-for="(user, index) in users" :key="user.id" 
          class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full overflow-hidden">
            <img 
              :src="user.avatar || '/placeholder.svg'" 
              :alt="user.name"
              class="w-full h-full object-cover"
            />
          </div>
          <div class="flex-1">
            <div class="flex items-center gap-2">
              <span class="font-medium">{{ user.name }}</span>
              <span class="px-2 py-0.5 rounded-full text-xs text-white"
                :class="getLevelBadgeClass(user.level)">
                Ур. {{ user.level }}
              </span>
            </div>
          </div>
          <div class="text-gray-400 font-medium">#{{ index + 1 }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { User } from 'lucide-vue-next'

const users = [
  { id: 1, name: 'Уаров Артем', level: 13, avatar: '/placeholder.svg' },
  { id: 2, name: 'Мария Петрова', level: 18, avatar: '/placeholder.svg' },
  { id: 3, name: 'Сергей Смирнов', level: 25, avatar: '/placeholder.svg' },
  { id: 4, name: 'Анна Васильева', level: 15, avatar: '/placeholder.svg' },
  { id: 5, name: 'Алексей Кузнецов', level: 22, avatar: '/placeholder.svg' },
  { id: 6, name: 'Елена Павлова', level: 21, avatar: '/placeholder.svg' },
  { id: 7, name: 'Айтал Попов', level: 20, avatar: '/placeholder.svg' },
  { id: 8, name: 'Виктор Соколов', level: 19, avatar: '/placeholder.svg' },
  { id: 9, name: 'Данил Трампов', level: 16, avatar: '/placeholder.svg' }
]

const getLevelBadgeClass = (level) => {
  const colors = {
    13: 'bg-orange-500',
    18: 'bg-yellow-500',
    25: 'bg-green-500',
    15: 'bg-purple-500',
    22: 'bg-purple-500',
    21: 'bg-purple-500',
    20: 'bg-blue-500',
    19: 'bg-blue-500',
    16: 'bg-blue-500'
  }
  return colors[level] || 'bg-gray-500'
}
</script>