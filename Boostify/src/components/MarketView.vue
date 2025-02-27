<template>
  <div class="px-4">
    <div class="grid gap-4">
      <div v-for="product in products" :key="product.id"
        class="bg-gray-50 rounded-xl overflow-hidden">
        <div class="aspect-[4/3] bg-gradient-to-br from-purple-500 to-blue-500 flex items-center justify-center">
          <img :src="product.image" :alt="product.name" class="w-full h-full object-cover" />
        </div>
        <div class="p-4">
          <h3 class="font-medium text-gray-900 mb-2">{{ product.name }}</h3>
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-1">
              <CircleDollarSign class="w-4 h-4 text-green-500" />
              <span class="font-medium text-green-500">{{ product.price }}</span>
            </div>
            <button class="px-4 py-2 bg-green-500 text-white rounded-lg text-sm font-medium">
              Купить
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { CircleDollarSign } from 'lucide-vue-next'

const products = [
  { 
    id: 1, 
    name: 'Толстовка BB', 
    price: '8500',
    image: '/placeholder.svg?height=300&width=400'
  },
  { 
    id: 2, 
    name: 'Кепка BB', 
    price: '2500',
    image: '/placeholder.svg?height=300&width=400'
  },
  { 
    id: 3, 
    name: 'Кружка BB', 
    price: '1500',
    image: '/placeholder.svg?height=300&width=400'
  },
  { 
    id: 4, 
    name: 'Значок BB', 
    price: '500',
    image: '/placeholder.svg?height=300&width=400'
  }
]
</script>