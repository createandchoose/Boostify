<template>
  <div class="continer">
    <div class="zag">Таски</div>

    <!-- Tabs -->
    <div class="tabs-menu w-tab-menu">
      <a v-for="tab in tabs" :key="tab.id" @click="currentTab = tab.id" data-w-tab="Tab 1"
        class="tabbb11c w-inline-block w-tab-link" :class="currentTab === tab.id ? 'w--current' : ''">
        <img src="../../b8stify.webflow.io/67bf26ad9cb30c9bdf27f087/67bf3d842cd0e8c51e6e431b_trophy.svg" width="24"
          height="24">
        <div class="text-20">{{ tab.name }}</div>
      </a>
    </div>




    <div v-if="currentTab === 'tasks'" class="space-y-4">
      <div v-for="task in tasks" :key="task.id" class="frame-44727">
        <!-- <div class="componentstatus">
                <div class="pending">В процессе</div>
            </div>
            <div class="componentstatus-4">
                <div class="pending-4">На проверке</div>
            </div>
            <div class="componentstatus-3">
                <div class="pending-3">Сделано</div>
            </div>
            <div class="componentstatus-2">
                <div class="pending-2">Провалено</div>
            </div> -->

        <div class="componentstatus-3">
          <div class="pending-3"> {{ task.status }}</div>
        </div>
        <div class="text-21">{{ task.title }}</div>
        <div class="text-22">{{ task.description }}</div>
        <div class="frame-2178">
          <div class="frame-2175">
            <div class="text-23">Награда:</div>
            <div class="frame-2179">
              <div class="text-24">⚡ {{ task.rewards.points }} Баллов</div>
              <div class="text-25">|</div><img
                src="../../b8stify.webflow.io/67bf26ad9cb30c9bdf27f087/67bf3e32c809cc85f7d64c2a_Frame-1114.svg"
                loading="lazy" width="18" height="18" alt="" class="frame-44728">
              <div class="text-24">{{ task.rewards.boost }} BOOST</div>
            </div>
          </div>
          <div class="frame-2175">
            <div class="text-23">Сроки:</div>
            <div class="text-22">{{ task.deadline }}</div>
          </div>
        </div>
        <div class="frame-44729">
          <div class="frame-65">
            <div class="component-9 elements"><img
                src="../../b8stify.webflow.io/67bf26ad9cb30c9bdf27f087/67bf3e338898d8365b6f0858_file-filled.svg"
                loading="lazy" width="24" height="24" alt="" class="file-filled">
              <div class="label-style"> {{ task.status === 'В процессе' ? 'Отправить на проверку' : 'На проверке' }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>


    <div v-if="currentTab === 'notifications'" class="lider">
      <div class="space-y-6">
      <div class="frame-44727">
        <div class="text-21">Сверхурочная работа</div>
        <div class="text-22">В случае возникновения срочных задач, требующих вашего внимания после окончания рабочего
          дня, проявите готовность остаться и завершить проект в срок. Ваше участие будет способствовать своевременному
          выполнению важных задач.</div>

      </div>



    </div>



  </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Star, CircleDollarSign, FileText } from 'lucide-vue-next'

const currentTab = ref('tasks')

const tabs = [
  { id: 'tasks', name: 'Задачи' },
  { id: 'notifications', name: 'Уведомления' }
]

const tasks = [
  {
    id: 1,
    status: 'В процессе',
    title: 'Сверхурочная работа',
    description: 'В случае возникновения срочных задач, требующих вашего внимания после окончания рабочего дня, проявите готовность остаться и завершить проект в срок. Ваше участие будет способствовать своевременному выполнению важных задач.',
    rewards: {
      points: 50,
      boost: 50
    },
    deadline: 'До 02.03.2025'
  },
  {
    id: 2,
    status: 'На проверке',
    title: 'Замещение отсутствующих коллег',
    description: 'В случае отсутствия ваших коллег по причине болезни или отпуска, принимайте на себя дополнительные функции, чтобы обеспечить бесперебойную работу отдела. Ваша гибкость и ответственность помогут нам справиться с любыми трудностями.',
    rewards: {
      points: 50,
      boost: 10
    },
    deadline: 'До 01.03.2025'
  }
]
</script>