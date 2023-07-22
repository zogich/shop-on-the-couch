<template>
  <n-layout>
    <n-tabs type="bar" animated>
      <n-tab-pane name="text" tab="Текст">
        <n-space>
          <editor-content :editor="editor" />
        </n-space>
      </n-tab-pane>
      <n-tab-pane name="settings" tab="Настройки">
        <n-layout>
        <n-space horizontal>
          <n-card>
            <h2>Название статьи</h2><n-input v-model:value="value" type="text" placeholder= {{article.name}} />
            <h2>Категория</h2><n-select v-model:value="value" :options="categoriesNames"></n-select>
          </n-card>
          <n-card>
            <h2>Загрузить обложку</h2>
            <n-upload directory-dnd action="" :max="1">
              <n-upload-dragger>
                <div style="margin-bottom: 12px">
                  <n-icon size="48" :depth="3">
                    <archive-icon />
                  </n-icon>
                </div>
                <h3>
                  Кликни или перетяни изображение
                </h3>
                <p depth="3" style="margin: 8px 0 0 0">
                  Если у тебя нет обложки, запроси его у дизайнера из контент-плана
                </p>
              </n-upload-dragger>
            </n-upload>
          </n-card>
          <n-card>
            <h2>SEO</h2>
            <h3>Ключевые слова</h3>
            <n-input v-model:value="value" type="text" placeholder="Введи ключевые слова" />
          </n-card>
        </n-space>
        </n-layout>
      </n-tab-pane>
    </n-tabs>
  </n-layout>
</template>

<script>
import { Editor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import api from '../../stores/api.js'
import {NButton, NLayout, NTabPane, NTabs, NSpace, NInput, NCard, NSelect, useMessage,
  NUpload, NUploadDragger} from 'naive-ui'
import useTokenStore from "~/stores/modules/token";
import useArticleStore from "~/stores/modules/article";
import {ref} from "vue";

export default {
  components: {
    EditorContent, NLayout, NButton, NTabs, NTabPane, NSpace, NInput, NCard, NSelect, NUpload, NUploadDragger
  },

  data() {
    return {
      editor: null,
    }
  },

  async setup(){
    const message = useMessage();
    const tokenStore = useTokenStore();
    const articleStore = useArticleStore();
    const categoriesNames = []
    await articleStore.fetchCategories();
    await articleStore.fetchAllArticles();
    articleStore.categories.forEach(element =>{
      categoriesNames.push({label: element.name, key: element.name})
    })
    const route = useRoute()
    let article = null;
    await api.get('/api/article/', {params: { id: route.params.id }}).then(response =>{
      article = response.data[0]
    })
    return {
      value: ref(null),
      handleSelect(key) {
        message.info(String(key))
      },
      tokenStore,
      articleStore,
      categoriesNames,
      route,
      article}
  },

  async mounted() {
    const route = useRoute()
    let text = null;
    await api.get('/api/article/', {params: { id: route.params.id }}).then(response =>{
      text = response.data[0]
    })
    this.editor = new Editor({
      content: text.text,
      extensions: [
        StarterKit,
      ],
    })
  },

  beforeDestroy() {
    this.editor.destroy()
  },
}
</script>