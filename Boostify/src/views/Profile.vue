`<template>
  <div class="p-4">
    <div class="bg-white rounded-lg shadow p-6"
         v-motion
         :initial="{ opacity: 0, y: 20 }"
         :enter="{ opacity: 1, y: 0 }">
      <div class="flex items-center mb-6">
        <div class="w-20 h-20 bg-blue-500 rounded-full flex items-center justify-center text-white text-2xl">
          {{ initials }}
        </div>
        <div class="ml-4">
          <h2 class="text-xl font-bold">{{ profile.name }}</h2>
          <p class="text-gray-600">{{ profile.position }}</p>
        </div>
      </div>
      
      <div class="space-y-4">
        <div class="border-b pb-4">
          <h3 class="text-sm text-gray-500 mb-2">Email</h3>
          <p>{{ profile.email }}</p>
        </div>
        
        <div class="border-b pb-4">
          <h3 class="text-sm text-gray-500 mb-2">Телефон</h3>
          <p>{{ profile.phone }}</p>
        </div>
        
        <div>
          <h3 class="text-sm text-gray-500 mb-2">Достижения</h3>
          <div class="flex flex-wrap gap-2">
            <span v-for="achievement in profile.achievements" 
                  :key="achievement"
                  class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">
              {{ achievement }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const profile = ref({
  name: 'Иван Петров',
  position: 'Старший менеджер',
  email: 'ivan@example.com',
  phone: '+7 (999) 123-45-67',
  achievements: ['Лучший сотрудник', 'Инноватор года', 'Командный лидер']
})

const initials = computed(() => {
  return profile.value.name
    .split(' ')
    .map(n => n[0])
    .join('')
})
</script>`