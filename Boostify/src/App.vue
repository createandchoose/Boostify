`<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Top header -->
    <header class="bg-blue-500 text-white p-4 fixed top-0 w-full z-50">
      <div class="flex items-center">
        <button @click="toggleMenu" class="mr-4">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
        <h1 class="text-xl font-semibold">{{ currentPage }}</h1>
      </div>
    </header>

    <!-- Main content -->
    <main class="pt-16 pb-20">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- Bottom navigation -->
    <nav class="fixed bottom-0 w-full bg-white border-t border-gray-200">
      <div class="flex justify-around p-4">
        <router-link to="/" class="flex flex-col items-center text-gray-600 hover:text-blue-500 transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
          </svg>
          <span class="text-sm">Главная</span>
        </router-link>
        <router-link to="/profile" class="flex flex-col items-center text-gray-600 hover:text-blue-500 transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
          <span class="text-sm">Профиль</span>
        </router-link>
        <router-link to="/shop" class="flex flex-col items-center text-gray-600 hover:text-blue-500 transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
          </svg>
          <span class="text-sm">Магазин</span>
        </router-link>
        <router-link to="/games" class="flex flex-col items-center text-gray-600 hover:text-blue-500 transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z" />
          </svg>
          <span class="text-sm">Мини игры</span>
        </router-link>
      </div>
    </nav>

    <!-- Side menu -->
    <transition name="slide">
      <div v-if="isMenuOpen" 
           class="fixed inset-0 bg-black bg-opacity-50 z-50"
           @click="toggleMenu">
        <div class="w-64 h-full bg-white shadow-lg"
             @click.stop>
          <div class="p-4 bg-blue-500 text-white">
            <h2 class="text-xl font-bold">Меню</h2>
          </div>
          <!-- Notifications Section -->
          <div class="p-4 border-b">
            <h3 class="font-medium text-gray-900 mb-3">Уведомления</h3>
            <div v-if="notifications.length > 0">
              <div v-for="notification in notifications" 
                   :key="notification.id"
                   class="mb-3 p-3 bg-gray-50 rounded-lg"
                   v-motion
                   :initial="{ opacity: 0, x: -20 }"
                   :enter="{ opacity: 1, x: 0 }">
                <p class="text-sm text-gray-800">{{ notification.message }}</p>
                <span class="text-xs text-gray-500 mt-1 block">{{ notification.time }}</span>
              </div>
            </div>
            <p v-else class="text-sm text-gray-500">Нет новых уведомлений</p>
          </div>
          <!-- Admin Panel Section -->
          <div class="p-4">
            <h3 class="font-medium text-gray-900 mb-3">Админ панель</h3>
            <div class="space-y-2">
              <button v-for="option in adminOptions" 
                      :key="option.id"
                      class="w-full text-left px-3 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded-lg transition-colors flex items-center"
                      v-motion
                      :initial="{ opacity: 0, x: -20 }"
                      :enter="{ opacity: 1, x: 0 }">
                <span class="mr-2">{{ option.icon }}</span>
                {{ option.name }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const isMenuOpen = ref(false)

const menuItems = [
  { path: '/', name: 'Главная' },
  { path: '/profile', name: 'Профиль' },
  { path: '/shop', name: 'Магазин' },
  { path: '/games', name: 'Мини игры' }
]

const notifications = ref([
  {
    id: 1,
    message: 'Новое достижение разблокировано!',
    time: '5 минут назад'
  },
  {
    id: 2,
    message: 'Ваш рейтинг повысился',
    time: '1 час назад'
  },
  {
    id: 3,
    message: 'Добавлены новые товары в магазин',
    time: '2 часа назад'
  }
])

const adminOptions = ref([
  {
    id: 1,
    name: 'Управление пользователями',
    icon: '👥'
  },
  {
    id: 2,
    name: 'Статистика',
    icon: '📊'
  },
  {
    id: 3,
    name: 'Настройки приложения',
    icon: '⚙️'
  },
  {
    id: 4,
    name: 'Управление контентом',
    icon: '📝'
  }
])

const currentPage = computed(() => {
  const current = menuItems.find(item => item.path === route.path)
  return current ? current.name : 'Главная'
})

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(-100%);
}
</style>`