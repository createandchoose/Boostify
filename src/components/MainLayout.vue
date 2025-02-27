<template>
    <main>
      <RouterView />
    </main>
    <nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-100">
      <div class="flex justify-around py-3">
        <RouterLink 
          v-for="tab in tabs" 
          :key="tab.id"
          :to="tab.path"
          class="flex flex-col items-center gap-1"
          :class="currentRoute === tab.path ? 'text-green-500' : 'text-gray-400'">
          <component :is="tab.icon" class="w-6 h-6" />
          <span class="text-xs">{{ tab.name }}</span>
        </RouterLink>
      </div>
    </nav>

</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { Home, FileText, ShoppingCart, User } from 'lucide-vue-next'

const route = useRoute()

const tabs = [
  { id: 'home', name: 'Главная', icon: Home, path: '/' },
  { id: 'tasks', name: 'Таски', icon: FileText, path: '/tasks' },
  { id: 'market', name: 'Маркет', icon: ShoppingCart, path: '/market' },
  { id: 'profile', name: 'Профиль', icon: User, path: '/profile' },
]

const currentRoute = computed(() => route.path)
</script>