<template>
  <n-config-provider>
  <n-layout-footer bordered position="relative">
    <h1>Logo</h1>
    <n-space horizontal style="gap: 3px" justify='space-between' align="start">
    <n-space vertical>
      <n-button type="tertiary">Связаться с нами</n-button>
      <a href="">Стать частью команды</a>
      <a href="">О нас</a>
    </n-space>
    <n-space vertical>
      <span>Каталог</span>
      <n-space>
        <n-space vertical>
          <a href="">Новости</a>
          <a href="">Люди</a>
          <a href="">Тренды</a>
          <a href="">Сообщества</a>
        </n-space>
        <n-space vertical>
          <a href="">Справочкник</a>
          <a href="">Спецпроект</a>
          <a href="">ASAP</a>
        </n-space>
      </n-space>
    </n-space>
    <n-space vertical>
      <span>Подпишись</span>
      <n-space vertical>
        <a href="">ВКонтакте</a>
        <a href="">Telegram</a>
      </n-space>
    </n-space>
    <div class="fourth-section">
      <span>Контакты</span>
      <n-space vertical>
        <a href="tel:+79009009090">+7 (900) 900-90-90</a>
        <a href="mailto: sail@mail.com">sail@mail.com</a>
      </n-space>
    </div>
    </n-space>
    <n-divider />
  </n-layout-footer>
  </n-config-provider>
</template>

<script>
import {NButton, NLayoutFooter, NSpace, NDivider, NConfigProvider} from 'naive-ui'
import { darkTheme } from 'naive-ui'

export default {
  name: "ShopFooter",
  components: {
    NButton, NLayoutFooter, NSpace, NDivider, NConfigProvider
  },
  setup() {
    return {
      darkTheme
    }
  }
}

</script>

<style scoped>

a {
  text-decoration: none;
}

.n-button {
  color: white;
}

.n-layout-footer {
  color: white;
  padding: 64px 96px;
  background-color: rgba(81, 85, 98, 1);
}

</style>