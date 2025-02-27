<template>
  <div class="min-h-screen bg-white">
    <div class="px-4 py-4">
      <h1 class="text-xl font-bold mb-6">Таски</h1>

      <!-- Status Filters -->
      <div class="space-y-2 mb-6">
        <button 
          class="w-full flex items-center justify-between p-4 rounded-xl bg-gray-50/50"
          @click="currentStatus = 'waiting'"
        >
          <span class="text-gray-900">В ожидании</span>
          <div class="flex items-center gap-2">
            <span class="text-sm text-gray-400">300 шт.</span>
            <ChevronRight class="w-5 h-5 text-gray-400" />
          </div>
        </button>

        <button 
          class="w-full flex items-center justify-between p-4 rounded-xl bg-blue-50/50"
          @click="currentStatus = 'in_progress'"
        >
          <span class="text-gray-900">В процессе</span>
          <div class="flex items-center gap-2">
            <span class="text-sm text-blue-400">24 шт.</span>
            <ChevronRight class="w-5 h-5 text-gray-400" />
          </div>
        </button>

        <button 
          class="w-full flex items-center justify-between p-4 rounded-xl bg-green-50/50"
          @click="currentStatus = 'completed'"
        >
          <span class="text-gray-900">Завершенные</span>
          <div class="flex items-center gap-2">
            <span class="text-sm text-green-400">124 шт.</span>
            <ChevronRight class="w-5 h-5 text-gray-500" />
          </div>
        </button>
      </div>

      <div class="text-sm text-gray-500 mb-4">Отправили на проверку</div>

      <!-- Task Details -->
      <div class="bg-gray-300 rounded-xl p-4">
        <div class="text-sm text-yellow-500 font-medium mb-4">На проверке</div>

        <div class="space-y-4">
          <h2 class="text-lg font-medium">Замещение отсутствующих коллег</h2>
          <p class="text-gray-600 text-sm">
            В случае отсутствия ваших коллег по причине болезни или отпуска, принимайте на себя дополнительные функции, чтобы обеспечить бесперебойную работу отдела. Ваша гибкость и ответственность помогут нам справиться с любыми трудностями.
          </p>

          <!-- Rewards -->
          <div class="flex items-center gap-4">
            <div class="flex items-center gap-1">
              <Star class="w-4 h-4 text-yellow-500" />
              <span class="text-sm">50 Баллов</span>
            </div>
            <div class="flex items-center gap-1">
              <CircleDollarSign class="w-4 h-4" />
              <span class="text-sm">10 BOOST</span>
            </div>
          </div>

          <div class="text-sm text-gray-500">
            Сроки: До 01.03.2025
          </div>

          <!-- Executor -->
          <div class="flex items-center gap-3 py-2">
            <div class="w-10 h-10 rounded-full bg-emerald-500 flex items-center justify-center">
              <User class="w-5 h-5 text-white" />
            </div>
            <div>
              <div class="font-medium">Айтал Попов</div>
              <div class="text-sm text-gray-500">Исполнитель</div>
            </div>
          </div>

          <!-- Actions -->
          <div class="grid gap-3">
            <button class="w-full py-3 bg-green-100 rounded-xl text-green-600 font-medium hover:bg-green-200 transition-colors">
              Утвердить
            </button>
            <button class="w-full py-3 bg-red-50 rounded-xl text-red-600 font-medium hover:bg-red-100 transition-colors">
              Отклонить
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ChevronRight, Star, CircleDollarSign, User } from 'lucide-vue-next'

const currentStatus = ref('in_progress')
</script>

