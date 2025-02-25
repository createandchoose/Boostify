`<template>
  <div class="p-4">
    <div class="grid grid-cols-2 gap-4">
      <div v-for="(game, index) in games" 
           :key="game.id" 
           class="bg-white rounded-lg shadow p-4 flex flex-col items-center"
           v-motion
           :initial="{ opacity: 0, y: 20 }"
           :enter="{ opacity: 1, y: 0, transition: { delay: index * 100 } }">
        <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mb-3">
          <span class="text-2xl">{{ game.emoji }}</span>
        </div>
        <h3 class="font-semibold text-center mb-2">{{ game.name }}</h3>
        <p class="text-gray-600 text-sm text-center mb-4">{{ game.description }}</p>
        <button class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition-colors w-full">
          Играть
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const games = ref([
  {
    id: 1,
    name: 'Память',
    description: 'Тренируйте память, находя пары карточек',
    emoji: '🎴'
  },
  {
    id: 2,
    name: 'Пазл',
    description: 'Собирайте картинки из частей',
    emoji: '🧩'
  },
  {
    id: 3,
    name: 'Квиз',
    description: 'Проверьте свои знания',
    emoji: '❓'
  },
  {
    id: 4,
    name: 'Змейка',
    description: 'Классическая игра змейка',
    emoji: '🐍'
  }
])
</script>`