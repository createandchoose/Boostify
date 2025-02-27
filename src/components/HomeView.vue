<template>


        <div class="continer">
            <div class="zag">Главная</div>

            <div class="text">Проекты</div>
            <div class="div-block-4">
                <div class="frame-44742">
                    <div class="frame-2201">
                        <a href="#" target="_blank" class="button-style-5 icon">
                            <div class="flash">
                                <div class="flash"></div><img src="" loading="lazy" width="14" height="14" alt=""
                                    class="flash-1">
                            </div>
                        </a>
                        <div class="text-37">Хакатон MPIT 2025</div>
                    </div>
                    <div class="frame-2202">
                        <div class="frame-44743">
                            <div class="frame-44744">
                                <div class="text-38">Команда</div>
                                <div class="frame-44745">
                                    <div class="frame-2197"></div>
                                    <div class="frame-2197"></div>
                                    <div class="frame-2197"></div>
                                    <div class="frame-2197"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <a href="#" class="frame-44746 w-inline-block">
                        <div class="text-39">Посмотреть проект</div>
                    </a>
                </div>
                <div class="frame-44742">
                    <div class="frame-2201">
                        <a href="#" target="_blank" class="button-style-5 icon">
                            <div class="flash">
                                <div class="flash"></div><img src="" loading="lazy" width="14" height="14" alt=""
                                    class="flash-1">
                            </div>
                        </a>
                        <div class="text-37">Хакатон MPIT 2025</div>
                    </div>
                    <div class="frame-2202">
                        <div class="frame-44743">
                            <div class="frame-44744">
                                <div class="text-38">Команда</div>
                                <div class="frame-44745">
                                    <div class="frame-2197"></div>
                                    <div class="frame-2197"></div>
                                    <div class="frame-2197"></div>
                                    <div class="frame-2197"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <a href="#" class="frame-44746 w-inline-block">
                        <div class="text-39">Посмотреть проект</div>
                    </a>
                </div>
            </div>


            <!-- Tabs -->
            <div class="tabs-menu w-tab-menu">
                <a v-for="tab in tabs" :key="tab.id" @click="currentTab = tab.id" data-w-tab="Tab 1"
                    class="tabbb11c w-inline-block w-tab-link" :class="currentTab === tab.id ? 'w--current' : ''">
                    <img src="../../b8stify.webflow.io/67bf26ad9cb30c9bdf27f087/67bf3d842cd0e8c51e6e431b_trophy.svg"
                        width="24" height="24">
                    <div class="text-20">{{ tab.name }}</div>
                </a>
            </div>




            <div v-if="currentTab === 'tasks'" class="space-y-4">
                <div class="text">Задачи</div>
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
                                <div class="label-style"> {{ task.status === 'В процессе' ? 'Отправить на проверку' :
                                    'На проверке' }}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


            <div v-if="currentTab === 'lider'" class="lider">
                <div class="text">Я</div>
                <div class="frame-447">
                    <div class="frame-68">
                        <div class="imgprof"><img src="" loading="lazy" alt=""></div>
                        <div class="content-style">
                            <div class="component-copy elements-copy">
                                <div class="text">Айтал Попов</div>
                                <div class="frame-1114">
                                    <div class="text-3">Ур. 20</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="component-2 elements">
                        <div class="text">#8</div>
                    </div>
                </div>
                <div class="div-block">
                    <div class="text21">Сотрудники</div>
                    <div class="texttt12">Топ 10</div>
                </div>
                <div class="div-block-3">
                    <div class="frame-44723">
                        <div class="frame-68">
                            <div class="imgprof"><img src="" loading="lazy" alt=""></div>
                            <div class="content-style">
                                <div class="component-copy elements-copy">
                                    <div class="text">Айтал Попов</div>
                                    <div class="frame-1114">
                                        <div class="text-3">Ур. 20</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="component-2 elements">
                            <div class="text">#8</div>
                        </div>
                    </div>
                    <div class="frame-44723">
                        <div class="frame-68">
                            <div class="imgprof"><img src="" loading="lazy" alt=""></div>
                            <div class="content-style">
                                <div class="component-copy elements-copy">
                                    <div class="text">Айтал Попов</div>
                                    <div class="frame-1114">
                                        <div class="text-3">Ур. 20</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="component-2 elements">
                            <div class="text">#8</div>
                        </div>
                    </div>
                    <div class="frame-44723">
                        <div class="frame-68">
                            <div class="imgprof"><img src="" loading="lazy" alt=""></div>
                            <div class="content-style">
                                <div class="component-copy elements-copy">
                                    <div class="text">Айтал Попов</div>
                                    <div class="frame-1114">
                                        <div class="text-3">Ур. 20</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="component-2 elements">
                            <div class="text">#8</div>
                        </div>
                    </div>
                </div>
            </div>




        </div>



</template>


<style>
.lider {
    grid-column-gap: 12px;
    grid-row-gap: 12px;
    flex-flow: column;
    display: flex;
    overflow: hidden;
}
</style>

<script setup>

import { ref } from 'vue'
import { Star, CircleDollarSign, FileText } from 'lucide-vue-next'

const currentTab = ref('tasks')

const tabs = [
    { id: 'tasks', name: 'Задачи' },
    { id: 'lider', name: 'Лидерборд' }
]

const tasks = [
    {
        id: 1,
        status: 'В процессе',
        title: 'Сверхурочфывфывфыабота',
        description: 'В случае возникновения срочных задач, требующих вашего внимания после окончания рабочего дня, проявите готовность остаться и завершить проект в срок. Ваше участие будет способствовать своевременному выполнению важных задач.',
        rewards: {
            points: 111150,
            boost: 111150
        },
        deadline: 'До 02.03.2025'
    },
    {
        id: 2,
        status: 'На проверке',
        title: 'Замещение отсутствующих коллег',
        description: 'В случае отсутствия ваших коллег по причине болезни или отпуска, принимайте на себя дополнительные функции, чтобы обеспечить бесперебойную работу отдела. Ваша гибкость и ответственность помогут нам справиться с любыми трудностями.',
        rewards: {
            points: 53450,
            boost: 12350
        },
        deadline: 'До 01.03.2025'
    }
]
</script>