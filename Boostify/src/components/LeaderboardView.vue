<template>
  <div class="min-h-screen bg-white">
    <!-- Top Navigation -->
    

    <div class="px-4 pb-4">
      <h1 class="text-2xl font-bold mb-6">Таблица лидеров</h1>

      <!-- Current User -->
      <div class="mb-6">
        <div class="text-sm font-medium text-gray-500 mb-3">Я</div>
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 rounded-full bg-emerald-500 flex items-center justify-center">
            <User class="w-6 h-6 text-white" />
          </div>
          <div class="flex-1">
            <div class="flex items-center gap-2">
              <span class="font-medium">Айтал Попов</span>
              <span class="px-2 py-0.5 bg-blue-100 text-blue-600 rounded-full text-xs font-medium">
                Ур. 20
              </span>
            </div>
          </div>
          <div class="text-gray-400 font-medium">#8</div>
        </div>
      </div>

      <!-- Employees List -->
      <div>
        <div class="flex items-center justify-between mb-3">
          <div class="text-sm font-medium text-gray-500">Сотрудники</div>
          <div class="text-sm text-gray-400">Топ 10</div>
        </div>

        <div class="space-y-4">
          <div v-for="user in users" :key="user.id" class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-full overflow-hidden">
              <img 
                :src="user.avatar || '/placeholder.svg'" 
                :alt="user.name"
                class="w-full h-full object-cover"
              />
            </div>
            <div class="flex-1">
              <div class="flex items-center gap-2">
                <span class="font-medium">{{ user.name }}</span>
                <span 
                  class="px-2 py-0.5 rounded-full text-xs font-medium"
                  :class="getLevelBadgeClass(user.level)"
                >
                  Ур. {{ user.level }}
                </span>
              </div>
            </div>
            <div class="text-gray-400 font-medium">#{{ user.rank }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { User, SmilePlus } from 'lucide-vue-next'

const users = [
  { id: 1, name: 'Уаров Артем', level: 13, rank: 1, avatar: '/placeholder.svg' },
  { id: 2, name: 'Мария Петрова', level: 18, rank: 2, avatar: '/placeholder.svg' },
  { id: 3, name: 'Сергей Смирнов', level: 25, rank: 3, avatar: '/placeholder.svg' },
  { id: 4, name: 'Анна Васильева', level: 15, rank: 4, avatar: '/placeholder.svg' },
  { id: 5, name: 'Алексей Кузнецов', level: 22, rank: 5, avatar: '/placeholder.svg' },
  { id: 6, name: 'Елена Павлова', level: 21, rank: 6, avatar: '/placeholder.svg' },
  { id: 7, name: 'Айтал Попов', level: 20, rank: 8, avatar: '/placeholder.svg' },
  { id: 8, name: 'Виктор Соколов', level: 19, rank: 9, avatar: '/placeholder.svg' },
  { id: 9, name: 'Данил Трампов', level: 16, rank: 10, avatar: '/placeholder.svg' },
]

const getLevelBadgeClass = (level) => {
  const badges = {
    13: 'bg-blue-100 text-blue-600',
    18: 'bg-yellow-100 text-yellow-600',
    25: 'bg-green-100 text-green-600',
    15: 'bg-purple-100 text-purple-600',
    22: 'bg-purple-100 text-purple-600',
    21: 'bg-purple-100 text-purple-600',
    20: 'bg-blue-100 text-blue-600',
    19: 'bg-blue-100 text-blue-600',
    16: 'bg-blue-100 text-blue-600',
  }
  return badges[level] || 'bg-gray-100 text-gray-600'
}
</script>