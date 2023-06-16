<template>
  <n-config-provider :theme="darkTheme">
  <n-layout-footer bordered>
    <n-space horizontal style="gap: 3px" justify='space-evenly' align="start">
    <div class="first-section">
      <h1>Logo</h1>
      <n-button type="tertiary">Связаться с нами</n-button>
      <a href="">Политика конфиденциальности</a>
      <a href="">Пользовательское соглашение</a>
    </div>
    <div class="second-section">
      <span>Каталог</span>
      <div class="links-section">
        <div class="links">
          <a href="">Одежда</a>
          <a href="">Обувь</a>
          <a href="">Верхняя одежда</a>
          <a href="">Домашняя одежда</a>
        </div>
        <div class="links">
          <a href="">Купальники</a>
          <a href="">Аксессуары</a>
          <a href="">Идеи для подарков</a>
          <a href="">Marina rinaldi</a>
        </div>
      </div>
    </div>
    <div class="third-section">
      <span>О компании</span>
      <div class="links">
        <a href="">О нас</a>
        <a href="">Контакты</a>
        <a href="">Доставка</a>
        <a href="">Оплата</a>
      </div>
    </div>
    <div class="fourth-section">
      <span>Контакты</span>
      <div class="contacts">
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
      </div>
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
  root {
    --proto06: rgba(81, 85, 98, 1);
  }

  n-layout-footer{
    background-color: var(--proto06);
  }

  .first-section {
    display: flex;
    flex-direction: column;
  }

  .links-section{
    display: flex;
    flex-direction: row;
  }

  .links {
    display: flex;
    flex-direction: column;
  }
</style>