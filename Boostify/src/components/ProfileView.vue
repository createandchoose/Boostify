<template>
  <div class="min-h-screen bg-white">
    <!-- Top Navigation -->
    

    <div class="px-4 pb-4">
      <h1 class="text-2xl font-bold mb-6">Мой профиль</h1>

      <!-- Profile Info -->
      <div class="flex items-center gap-3 mb-4">
        <div class="w-12 h-12 rounded-full bg-emerald-500 flex items-center justify-center">
          <User class="w-6 h-6 text-white" />
        </div>
        <div class="flex-1">
          <div class="flex items-center gap-2">
            <h2 class="font-medium">Айтал Попов</h2>
            <span class="px-2 py-0.5 bg-blue-100 text-blue-600 rounded text-xs font-medium">
              Ур. 20
            </span>
          </div>
          <div class="flex items-center gap-2 text-sm">
            <span class="text-gray-500">Сотрудник</span>
            <span class="text-gray-400">•</span>
            <span class="text-gray-500">Рейтинг #8</span>
          </div>
        </div>
      </div>

      <!-- Progress Bar -->
      <div class="mb-6">
        <div class="h-2 bg-gray-100 rounded-full mb-2">
          <div class="h-full w-[65%] bg-gradient-to-r from-green-500 to-emerald-400 rounded-full"></div>
        </div>
        <div class="flex items-center justify-between text-sm">
          <span class="text-gray-600">65 из 100</span>
          <div class="flex items-center gap-1">
            <span class="text-gray-500">Еще 45 до</span>
            <span class="px-2 py-0.5 bg-purple-100 text-purple-600 rounded text-xs font-medium">
              41 Ур.
            </span>
          </div>
        </div>
      </div>

      <!-- Balance Card -->
      <div class="bg-gradient-to-r from-green-500 to-emerald-400 rounded-2xl p-4 mb-6">
        <div class="text-white/80 text-sm mb-1">Текущий баланс</div>
        <div class="flex items-baseline gap-1">
          <CircleDollarSign class="w-5 h-5 text-white" />
          <span class="text-3xl font-bold text-white">450.00</span>
        </div>
        <div class="text-white/90 text-sm mt-1">BOOST Коины</div>
      </div>

      <!-- Stats Grid -->
      <div class="grid grid-cols-3 gap-4">
        <div class="bg-gray-50 rounded-xl p-4 text-center">
          <div class="w-10 h-10 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-2">
            <Trophy class="w-5 h-5 text-orange-600" />
          </div>
          <div class="font-medium mb-1">Достижения</div>
          <div class="text-sm text-gray-500">Получено: 34</div>
        </div>

        <div class="bg-gray-50 rounded-xl p-4 text-center">
          <div class="w-10 h-10 bg-pink-100 rounded-full flex items-center justify-center mx-auto mb-2">
            <CheckCircle class="w-5 h-5 text-pink-600" />
          </div>
          <div class="font-medium mb-1">Сделано</div>
          <div class="text-sm text-gray-500">Тасков: 34</div>
        </div>

        <div class="bg-gray-50 rounded-xl p-4 text-center">
          <div class="w-10 h-10 bg-yellow-100 rounded-full flex items-center justify-center mx-auto mb-2">
            <Star class="w-5 h-5 text-yellow-600" />
          </div>
          <div class="font-medium mb-1">Награды</div>
          <div class="text-sm text-gray-500">Всего: 4</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { User, SmilePlus, CircleDollarSign, Trophy, CheckCircle, Star } from 'lucide-vue-next'
</script>