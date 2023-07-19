<template>
  <n-loading-bar-provider>
    <n-message-provider>
      <n-notification-provider>
        <n-dialog-provider>
          <ShopHeader />
          <div style="padding: 10px 96px">
          <NuxtPage />
          </div>

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

<script>

import ShopHeader from "/components/ShopHeader"
import ShopFooter from "/components/ShopFooter.vue"
import {NMessageProvider, NLoadingBarProvider, NNotificationProvider, NDialogProvider} from 'naive-ui'

export default {
  name: 'App',
  components: {ShopFooter, ShopHeader, NMessageProvider, NLoadingBarProvider, NNotificationProvider,
  NDialogProvider},
}

</script>