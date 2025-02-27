import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0', // Привязка ко всем интерфейсам
    port: 80, // Порт (можно изменить)
    allowedHosts: [
        'home.thefoxxstuff.net', // Разрешаем твой домен
        'localhost', // Для локального доступа
        '192.168.x.x' // Твой локальный IP (замени на актуальный)
    ]
},
})