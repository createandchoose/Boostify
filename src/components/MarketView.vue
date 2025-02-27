<template>


<div class="continer-dark">




        <div class="zag-d">Магазин</div>

        <a
         class="section-style-3">
            <div v-for="tab in tabs" :key="tab.id" @click="currentTab = tab.id" data-w-tab="Tab 1"
             class="frame-44725" :class="currentTab === tab.id ? 'w--currentt' : ''">
                
                    <div class="holocostas">{{ tab.name }}</div>
                
            </div>
        </a>



        <div v-if="currentTab === 'merch'" class="space-y-4">




        <div class="text-dark">Мерч компании</div>

        <div class="frame-2204"><img src="../../b8stify.webflow.io/67bf26ad9cb30c9bdf27f087/67bf4347c12d1955a383891e_Frame%202171.jpg" loading="lazy" class="image">
            <div class="frame-2205">
                <div class="text-26">Толстовка B8</div>
                <div class="frame-59">
                    <div class="frame-44730"><img src="../../b8stify.webflow.io/67bf26ad9cb30c9bdf27f087/67bf41227a5f33e953f3e81b_Frame-1115.svg" loading="lazy" width="24" height="24" alt="" class="frame-1115">
                        <div class="text-27">600,00</div>
                    </div>
                    <div class="frame-44731">
                        <div class="text-28">BOOST Коинов</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="frame-2204"><img src="../../b8stify.webflow.io/67bf26ad9cb30c9bdf27f087/67bf427908e737648858f89c_tovar.png" loading="lazy" alt="" class="image">
            <div class="frame-2205">
                <div class="text-26">Кепка B8</div>
                <div class="frame-59">
                    <div class="frame-44730"><img src="../../b8stify.webflow.io/67bf26ad9cb30c9bdf27f087/67bf41227a5f33e953f3e81b_Frame-1115.svg" loading="lazy" width="24" height="24" alt="" class="frame-1115">
                        <div class="text-27">600,00</div>
                    </div>
                    <div class="frame-44731">
                        <div class="text-28">BOOST Коинов</div>
                    </div>
                </div>
            </div>
        </div>

    </div>



    <div v-if="currentTab === 'buy'" class="space-y-4">


        <div class="frame-2185">
            <div class="text-dark">26.02.2025</div>
            <div class="frame-44747">
                <div class="frame-44748">
                    <div class="text-41">Толстовка B8</div>
                    <div class="text-42">26.02.2025 - 01:11</div>
                </div>
                <div class="co4353">
                    <div class="text-43">-800 BOOST</div>
                </div>
            </div>
        </div>

        <br><br><br><br><br><br><br><br><br><br><br><br><br>
        <br><br><br><br>


        </div>
<!-- ПОП АП ДОЛЖЕН БЫТЬ -->
        <div class="frame-44733">
            <div class="frame-44734">
                <div class="text-32">Толстовка B8</div>
                <div class="text-33-copy">Есть размеры XS, S</div>
            </div>
            <div class="frame-44735">
                <div class="frame-44736"><img src="../../b8stify.webflow.io/67bf26ad9cb30c9bdf27f087/67bf2af63cef5a3c5753b102_Frame-1114.svg" loading="lazy" width="24" height="24" alt="" class="frame-44737">
                    <div class="component-14 elements">
                        <div class="label-style-2">КУПИТЬ ЗА 800,00 BOOST</div>
                    </div>
                </div>
            </div>
        </div>
    </div>


</template>

<style>

</style>

<script setup>
import { ref } from 'vue'
const currentTab = ref('merch')

const tabs = [
  { id: 'merch', name: 'Мерч' },
  { id: 'buy', name: 'Покупки' }
]
</script>