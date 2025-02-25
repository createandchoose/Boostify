`<template>
  <div class="p-4">
    <div class="grid grid-cols-2 gap-4">
      <div v-for="(item, index) in items" 
           :key="item.id" 
           class="bg-white rounded-lg shadow overflow-hidden"
           v-motion
           :initial="{ opacity: 0, y: 20 }"
           :enter="{ opacity: 1, y: 0, transition: { delay: index * 100 } }">
        <img :src="item.image" :alt="item.name" class="w-full h-40 object-cover">
        <div class="p-4">
          <h3 class="font-semibold mb-2">{{ item.name }}</h3>
          <p class="text-gray-600 text-sm mb-3">{{ item.description }}</p>
          <div class="flex items-center justify-between">
            <span class="font-bold text-blue-600">{{ item.price }} ₽</span>
            <button class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition-colors">
              Купить
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
  {
    id: 1,
    name: 'Футболка',
    description: 'Стильная футболка с логотипом компании',
    price: 1500,
    image: 'https://via.placeholder.com/300x200'
  },
  {
    id: 2,
    name: 'Кружка',
    description: 'Керамическая кружка с принтом',
    price: 500,
    image: 'https://via.placeholder.com/300x200'
  },
  {
    id: 3,
    name: 'Рюкзак',
    description: 'Удобный рюкзак для ноутбука',
    price: 2500,
    image: 'https://via.placeholder.com/300x200'
  },
  {
    id: 4,
    name: 'Блокнот',
    description: 'Блокнот в твердой обложке',
    price: 300,
    image: 'https://via.placeholder.com/300x200'
  }
])
</script>`