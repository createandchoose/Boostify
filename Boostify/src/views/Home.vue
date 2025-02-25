`<template>
  <div class="p-4">
    <div class="bg-white rounded-lg shadow p-4 mb-4">
      <h2 class="text-xl font-bold mb-4">Рейтинг сотрудников</h2>
      <div v-for="(employee, index) in employees" 
           :key="employee.name"
           class="flex items-center justify-between p-3 border-b last:border-0"
           v-motion
           :initial="{ opacity: 0, y: 20 }"
           :enter="{ opacity: 1, y: 0, transition: { delay: index * 100 } }">
        <div class="flex items-center">
          <span class="mr-3 text-gray-600">{{ index + 1 }}.</span>
          <span class="font-medium">{{ employee.name }}</span>
        </div>
        <span class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">
          {{ employee.points }} баллов
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const employees = ref([
  { name: 'Иван', points: 100 },
  { name: 'Мария', points: 95 },
  { name: 'Алексей', points: 90 },
  { name: 'Елена', points: 85 },
  { name: 'Дмитрий', points: 80 }
])
</script>`