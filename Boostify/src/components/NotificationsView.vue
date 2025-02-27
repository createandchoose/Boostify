<template>
  <div class="px-4">
    <div class="space-y-3">
      <div v-for="notification in notifications" :key="notification.id"
        class="p-4 bg-gray-50 rounded-xl">
        <div class="flex items-start gap-3">
          <div class="p-2 rounded-lg" :class="notification.iconBg">
            <component :is="notification.icon" class="w-5 h-5" :class="notification.iconColor" />
          </div>
          <div class="flex-1">
            <h3 class="font-medium text-gray-900 mb-1">{{ notification.title }}</h3>
            <p class="text-sm text-gray-500">{{ notification.message }}</p>
            <span class="text-xs text-gray-400 mt-2 block">{{ notification.time }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Bell, Award, CreditCard } from 'lucide-vue-next'

const notifications = [
  {
    id: 1,
    title: 'Новое достижение',
    message: 'Вы получили награду за выполнение всех заданий!',
    time: '2 часа назад',
    icon: Award,
    iconBg: 'bg-yellow-100',
    iconColor: 'text-yellow-600'
  },
  {
    id: 2,
    title: 'Начисление баланса',
    message: 'На ваш счет начислено 1000 бонусов',
    time: '5 часов назад',
    icon: CreditCard,
    iconBg: 'bg-green-100',
    iconColor: 'text-green-600'
  }
]
</script>