<template>
  <n-config-provider>
  <n-layout-header bordered>
    <div class="bottom-header">
      <n-space horizontal style="gap: 3px" justify='space-between' align="baseline">
        <h1>Logo</h1>
        <div class="search-tab">
        <n-dropdown
            @select="handleSelect"
            :options="this.categories"
            placement="bottom-start"
            trigger="hover">
          <n-button color="#616575">Категории</n-button>
        </n-dropdown>
        <n-input v-model:value="value" type="text" placeholder="Поиск по статьям" />
        </div>
        <n-space horizontal>
          <a href="">Избранное</a>
          <a href="">Вход/Регистрация</a>
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
      handleSelect(key) {
        message.info(String(key))
      },
    }
  },

  data() {
    return{
      categories: [],
    }
  },
  methods() {

  },

  async created(){
    await this.$store.dispatch('fetchCategories');
    this.$store.state.article.categories.forEach(element =>{
      this.categories.push({label: element.name, key: element.name})
    })
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