<script setup>
import { RouterLink, RouterView } from 'vue-router'
import ShopHeader from "./components/ShopHeader.vue"
import ShopFooter from "./components/ShopFooter.vue"
import {NMessageProvider, NLoadingBarProvider, NNotificationProvider, NDialogProvider} from 'naive-ui'

</script>

<template>
  <n-loading-bar-provider>
    <n-message-provider>
      <n-notification-provider>
        <n-dialog-provider>
          <ShopHeader />
          <div style="padding: 10px 96px">
          <RouterView />
          </div>
          <ShopFooter />
        </n-dialog-provider>
      </n-notification-provider>
    </n-message-provider>
  </n-loading-bar-provider>
</template>

<style scoped>
 .page-container {
   /*display: flex;*/
   /*flex-direction: column;*/
 }
</style>
