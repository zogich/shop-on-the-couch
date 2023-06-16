<template>
  <n-config-provider>
  <n-layout-footer bordered>
    <h1>Logo</h1>
    <n-space horizontal style="gap: 3px" justify='space-between' align="start">
    <n-space vertical>
      <n-button type="tertiary">Связаться с нами</n-button>
      <a href="">Политика конфиденциальности</a>
      <a href="">Пользовательское соглашение</a>
    </n-space>
    <n-space vertical>
      <span>Каталог</span>
      <n-space>
        <n-space vertical>
          <a href="">Одежда</a>
          <a href="">Обувь</a>
          <a href="">Верхняя одежда</a>
          <a href="">Домашняя одежда</a>
        </n-space>
        <n-space vertical>
          <a href="">Купальники</a>
          <a href="">Аксессуары</a>
          <a href="">Идеи для подарков</a>
          <a href="">Marina rinaldi</a>
        </n-space>
      </n-space>
    </n-space>
    <n-space vertical>
      <span>О компании</span>
      <n-space vertical>
        <a href="">О нас</a>
        <a href="">Контакты</a>
        <a href="">Доставка</a>
        <a href="">Оплата</a>
      </n-space>
    </n-space>
    <div class="fourth-section">
      <span>Контакты</span>
      <n-space vertical>
        <a href="tel:+79009009090">+7 (900) 900-90-90</a>
        <a href="mailto: sail@mail.com">sail@mail.com</a>
        <div class="socials">
          <img src="" alt="">
          <img src="" alt="">
          <img src="" alt="">
          <img src="" alt="">
          <img src="" alt="">
          <img src="" alt="">
        </div>
      </n-space>
    </div>
    </n-space>
  </n-layout-footer>
  </n-config-provider>
</template>

<script>
import {NButton, NLayoutFooter, NSpace} from 'naive-ui'
import { darkTheme } from 'naive-ui'

export default {
  name: "ShopFooter",
  components: {
    NButton, NLayoutFooter, NSpace
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