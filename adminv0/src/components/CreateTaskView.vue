<template>
  <div class="min-h-screen bg-white">
    <div class="px-4 py-4">
      <h1 class="text-xl font-bold mb-6">Создать таск</h1>
      
      <div class="text-sm text-gray-500 mb-4">Отправили на проверку</div>

      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- Title -->
        <div>
          <input
            type="text"
            v-model="form.title"
            placeholder="Заголовок"
            class="w-full px-4 py-3 rounded-lg border border-gray-400 focus:outline-none focus:ring-2 focus:ring-green-500"
          />
        </div>

        <!-- Description -->
        <div>
          <textarea
            v-model="form.description"
            placeholder="Описание"
            rows="4"
            class="w-full px-4 py-3 rounded-lg border border-gray-400 focus:outline-none focus:ring-2 focus:ring-green-500"
          ></textarea>
        </div>

        <!-- Rewards -->
        <div>
          <h3 class="font-medium mb-3">Награда</h3>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <div class="flex items-center gap-1 mb-2">
                <Star class="w-4 h-4 text-yellow-500" />
                <span class="text-sm">Баллов</span>
              </div>
              <input
                type="number"
                v-model="form.points"
                placeholder="Баллов"
                class="w-full px-4 py-3 rounded-lg border border-gray-400 focus:outline-none focus:ring-2 focus:ring-green-500"
              />
            </div>
            <div>
              <div class="flex items-center gap-1 mb-2">
                <CircleDollarSign class="w-4 h-4" />
                <span class="text-sm">BOOST</span>
              </div>
              <input
                type="number"
                v-model="form.boost"
                placeholder="Boost"
                class="w-full px-4 py-3 rounded-lg border border-gray-400 focus:outline-none focus:ring-2 focus:ring-green-500"
              />
            </div>
          </div>
        </div>

        <!-- Submit -->
        <button
          type="submit"
          class="w-full py-3 bg-gray-100 rounded-lg text-gray-600 font-medium flex items-center justify-center gap-2"
        >
          <FileText class="w-5 h-5" />
          Добавить таск
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Star, CircleDollarSign, FileText } from 'lucide-vue-next'

const form = ref({
  title: '',
  description: '',
  points: '',
  boost: ''
})

const handleSubmit = () => {
  console.log('Form submitted:', form.value)
}
</script>