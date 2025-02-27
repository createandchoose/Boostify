<template>
  <div class="min-h-screen bg-white">
    <div class="px-4 pt-4">
      <h1 class="text-2xl font-bold mb-4">Главная</h1>

      <!-- Tabs -->
      <div class="flex gap-2 mb-6">
        <button 
          class="px-4 py-2 rounded-full text-sm"
          :class="{'bg-gray-100 font-medium': true}"
        >
          Задания
        </button>
        <RouterLink 
          to="/leaderboard"
          class="px-4 py-2 rounded-full text-sm text-gray-500 hover:bg-gray-50"
        >
          Лидерборд
        </RouterLink>
      </div>

      <!-- Competitions -->
      <div class="mb-6">
        <h2 class="text-lg font-medium mb-3">Соревнования</h2>
        <div class="flex gap-4 overflow-x-auto pb-4">
          <div class="min-w-[200px] h-[120px] rounded-2xl bg-purple-600 p-4 flex flex-col justify-between text-white">
            <h3 class="font-medium">Название компании</h3>
            <p class="text-sm text-white/80">До 8 марта придумать название</p>
          </div>
          <div class="min-w-[200px] h-[120px] rounded-2xl bg-pink-400 p-4 flex flex-col justify-between text-white">
            <h3 class="font-medium">Название компании</h3>
            <p class="text-sm text-white/80">До 8 марта придумать название</p>
          </div>
        </div>
      </div>

      <!-- Tasks -->
      <div>
        <h2 class="text-lg font-medium mb-3">Задачи</h2>
        <div class="space-y-4">
          <div v-for="task in tasks" :key="task.id" class="p-4 bg-gray-50 rounded-xl">
            <h3 class="font-medium mb-2">{{ task.title }}</h3>
            <p class="text-sm text-gray-600 mb-4">{{ task.description }}</p>
            <div class="flex items-center gap-4 mb-3">
              <div class="flex items-center gap-1">
                <Star class="w-4 h-4 text-yellow-500" />
                <span class="text-sm">{{ task.points }} Баллов</span>
              </div>
              <div class="flex items-center gap-1">
                <CircleDollarSign class="w-4 h-4" />
                <span class="text-sm">{{ task.boost }} BOOST</span>
              </div>
            </div>
            <div class="flex items-center justify-between">
              <div class="text-sm text-gray-500">
                Сроки: {{ task.deadline }}
              </div>
              <button class="flex items-center gap-2 text-sm text-gray-600">
                <FileText class="w-4 h-4" />
                Взять задачу
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { Star, CircleDollarSign, FileText } from 'lucide-vue-next'

const tasks = [
  {
    id: 1,
    title: 'Сверхурочная работа',
    description: 'В случае возникновения срочных задач, требующих вашего внимания после окончания рабочего дня, проявите готовность остаться и завершить проект в срок.',
    points: 50,
    boost: 50,
    deadline: 'До 02.03.2025'
  },
  {
    id: 2,
    title: 'Обучение новых сотрудников',
    description: 'Делитесь своими знаниями и опытом с новичками, помогая им адаптироваться и быстро осваивать необходимые навыки.',
    points: 50,
    boost: 50,
    deadline: 'До 02.03.2025'
  }
]
</script>