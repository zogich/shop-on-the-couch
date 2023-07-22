<template>
  <n-config-provider>
  <n-layout-header bordered>
    <div class="bottom-header">
      <n-space horizontal style="gap: 3px" justify='space-between' align="baseline">
        <h1>Logo</h1>
        <n-input-group>
        <n-dropdown
            @select="handleSelect"
            :options="categoriesNames"
            placement="bottom-start"
            trigger="hover">
          <n-button color="#616575">Категории</n-button>
        </n-dropdown>
        <n-input v-model:value="value" type="text" placeholder="Поиск по статьям" />
        </n-input-group>
        <n-space horizontal>
          <a href="">Избранное</a>
          <router-link :to="'/login'">Вход/Регистрация</router-link>
          <router-link v-if="tokenStore.isAuthenticated" :to="'/magazine-admin'">Админка</router-link>
        </n-space>
      </n-space>
    </div>
  </n-layout-header>
  </n-config-provider>
</template>

<script setup>

</script>

<script>
import {NButton, NLayoutHeader, NSpace, NDropdown, NInput, NConfigProvider, NInputGroup} from 'naive-ui'
import { useMessage } from 'naive-ui'
import {defineComponent, ref} from 'vue'
  import useTokenStore from "../stores/modules/token";
  import useArticleStore from "../stores/modules/article";

export default defineComponent({
  name: "ShopHeader",
  components: {
    NButton, NLayoutHeader, NSpace, NDropdown, NInput, NConfigProvider, NInputGroup
  },
  async setup() {
    const message = useMessage();
    const tokenStore = useTokenStore();
    const articleStore = useArticleStore();
    const categoriesNames = []
    await articleStore.fetchCategories();
    await articleStore.fetchAllArticles();
    articleStore.categories.forEach(element =>{
      categoriesNames.push({label: element.name, key: element.name})
    })
    return {
      value: ref(null),
      handleSelect(key) {
        message.info(String(key))
      },
      tokenStore,
      articleStore,
      categoriesNames,
    }
  },

  methods() {

  },

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


</style>