<template>
  <n-config-provider>
  <n-layout-header bordered>
    <div class="top-header">
    <n-space horizontal style="gap: 3px" justify='space-between' align="start">
      <n-space>
        <a href="">Контакты</a>
        <a href="">О нас</a>
        <a href="">Доставка</a>
      </n-space>
      <n-space>
        <a href="">logo</a>
        <a href="">Написать нам</a>
      </n-space>
    </n-space>
    </div>
    <div class="bottom-header">
      <n-space horizontal style="gap: 3px" justify='space-between' align="baseline">
        <h1>Logo</h1>
        <div class="search-tab">
        <n-dropdown
            @select="handleSelect"
            :options="options"
            placement="bottom-start"
            trigger="hover">
          <n-button color="#616575">Каталог</n-button>
        </n-dropdown>
        <n-input v-model:value="value" type="text" placeholder="Че ищем?" />
        </div>
        <n-space horizontal>
          <a href="">Избранное</a>
          <a href="">Вход/Регистрация</a>
          <a href="">Корзина</a>
        </n-space>
      </n-space>
    </div>
  </n-layout-header>
  </n-config-provider>
</template>

<script>
import {NButton, NLayoutHeader, NSpace, NDropdown, NInput} from 'naive-ui'
import { darkTheme, useMessage} from 'naive-ui'
import {defineComponent, ref} from 'vue'

export default defineComponent({
  name: "ShopHeader",
  components: {
    NButton, NLayoutHeader, NSpace, NDropdown, NInput
  },
  setup() {
    const message = useMessage();
    return {
      value: ref(null),
      options: [
        {
          label: 'Одежда',
          key: 'marina bay sands',
        },
        {
          label: "Обувь",
          key: "brown's hotel, london"
        },
        {
          label: 'Верхняя одежда',
          key: 'atlantis nahamas, nassau'
        },
        {
          label: 'Домашняя одежда',
          key: 'the beverly hills hotel, los angeles'
        },
        {
          label: 'Купальники',
          key: 'atlantis nahamas, nassau'
        },
        {
          label: 'Аксессуары',
          key: 'atlantis nahamas, nassau'
        },
        {
          label: 'Идеи для подарков',
          key: 'atlantis nahamas, nassau'
        },
        {
          label: 'Marina rinaldi',
          key: 'atlantis nahamas, nassau'
        }
      ],
      handleSelect(key) {
        message.info(String(key))
      }
    }
  }
})

</script>

<style scoped>

.bottom-header > a {
 text-decoration: none;
  color: white;
}

.top-header{
  background-color: rgba(81, 85, 98, 1);
  padding: 12px 96px;
}

.bottom-header{
  padding: 0 100px;
}

.search-tab {
  display: flex;
}

</style>