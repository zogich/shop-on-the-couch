<template>
  <n-layout>
  <n-tabs type="line" animated>
    <n-tab-pane name="articles" tab="Список статей">
      <n-space vertical>
        <n-table striped :single-line="false">
          <thead>
          <tr>
            <th>Название статьи</th>
            <th>Категория</th>
            <th>Дата публикации</th>
            <th>Действия</th>
          </tr>
          </thead>
          <tbody v-for="item in articleStore.articles" :key="item.id">
          <tr>
            <td>{{item.name}}</td>
            <td>{{item.category}}</td>
            <td>{{item.publication_date}}</td>
            <td>Пасхальные и музыкальные</td>
            <td>Люди</td>
            <td>01.01.2001</td>
            <td>
              <n-space>
                <n-button type="warning">Редактировать</n-button>
                <n-button type="error">Удалить</n-button>
                <n-switch v-model:value="active" size="large">
                  <template #checked-icon>
                    <n-icon :component="EyeOutline" />
                  </template>
                  <template #unchecked-icon>
                    <n-icon :component="EyeOffOutline" />
                  </template>
                </n-switch>
              </n-space>
            </td>
          </tr>
          </tbody>
        </n-table>
        </n-space>
    </n-tab-pane>
    <n-tab-pane name="users" tab="Пользователи">
      <n-space vertical>
        <n-table striped :single-line="false">
          <thead>
          <tr>
            <th>Имя пользователя</th>
            <th>Дата регистрации</th>
            <th>Роль</th>
            <th>Действия</th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <td>Kirill Pogranichniy</td>
            <td>20.06.2023</td>
            <td>Читатель</td>
            <td>
              <n-space>
                <n-button type="primary">Назначить администратором</n-button>
                <n-button type="error">Заблокировать</n-button>
              </n-space>
            </td>
          </tr>
          </tbody>
        </n-table>
      </n-space>
    </n-tab-pane>
  </n-tabs>
  </n-layout>
</template>

<script>
import {NTabs, NTabPane, NSpace, NTable, NSwitch, NIcon, NLayout, NButton} from "naive-ui";
import { defineComponent, ref } from "vue";
import { EyeOutline, EyeOffOutline } from "@vicons/ionicons5";
import useArticleStore from "../stores/modules/article";


export default defineComponent({
  name: "MagazineAdminView",
  components: {
    NTabs, NTabPane, NSpace, NTable, NSwitch, NIcon, NLayout, NButton
  },
  setup() {
    const articleStore = useArticleStore();
    return {
      active: ref(false),
      EyeOutline,
      EyeOffOutline,
      articleStore
    }
  },
  data(){
    return {
    }
  },
});
</script>

<style scoped>

</style>