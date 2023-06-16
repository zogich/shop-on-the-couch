<script setup>
import { RouterLink, RouterView } from 'vue-router'
import ShopHeader from "./components/ShopHeader.vue"
import ShopFooter from "./components/ShopFooter.vue"
import {NMessageProvider} from 'naive-ui'

</script>

<template>
  <n-message-provider>
    <ShopHeader />
    <RouterView />
    <ShopFooter />
  </n-message-provider>
</template>

<style scoped>
 .page-container {
   /*display: flex;*/
   /*flex-direction: column;*/
 }
</style>
