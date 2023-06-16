<script setup>
import { RouterLink, RouterView } from 'vue-router'
import ShopHeader from "./components/ShopHeader.vue"
import ShopFooter from "./components/ShopFooter.vue"

</script>

<template>
  <div class="page-container">
    <ShopHeader />
    <RouterView />
    <ShopFooter />
  </div>
</template>

<style scoped>
 .page-container {
   /*display: flex;*/
   /*flex-direction: column;*/
 }
</style>
