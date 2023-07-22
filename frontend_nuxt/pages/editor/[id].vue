<template>
  <n-layout>
    <n-tabs type="bar" animated>
      <n-tab-pane name="text" tab="Текст">
        <n-layout has-sider>
          <n-layout-sider
              bordered
              show-trigger
              collapse-mode="width"
              :collapsed-width="0"
              :width="240"
              :native-scrollbar="false"
              :inverted="inverted"
          >
            <n-space vertical v-if="editor">
              <bubble-menu
                  class="bubble-menu"
                  :tippy-options="{ duration: 100 }"
                  :editor="editor"
              >
                <button @click="editor.chain().focus().toggleBold().run()" :class="{ 'is-active': editor.isActive('bold') }">
                  Жирный
                </button>
                <button @click="editor.chain().focus().toggleItalic().run()" :class="{ 'is-active': editor.isActive('italic') }">
                  Курсив
                </button>
                <button @click="editor.chain().focus().toggleStrike().run()" :class="{ 'is-active': editor.isActive('strike') }">
                  Зачеркнутый
                </button>
              </bubble-menu>

              <floating-menu
                  class="floating-menu"
                  :tippy-options="{ duration: 100 }"
                  :editor="editor"
              >
                <button @click="editor.chain().focus().toggleHeading({ level: 1 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }">
                  Заголовок
                </button>
                <button @click="editor.chain().focus().toggleHeading({ level: 2 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }">
                  Подзаголовок
                </button>
                <button @click="editor.chain().focus().toggleBulletList().run()" :class="{ 'is-active': editor.isActive('bulletList') }">
                  Маркированный список
                </button>
              </floating-menu>
              <h3>Оформление текста</h3>
              <n-button @click="editor.chain().focus().toggleCode().run()" :class="{ 'is-active': editor.isActive('code') }">
                Код
              </n-button>
              <n-button @click="editor.chain().focus().toggleCodeBlock().run()" :class="{ 'is-active': editor.isActive('codeBlock') }">
                Блок кода
              </n-button>
              <n-button @click="editor.chain().focus().toggleBlockquote().run()" :class="{ 'is-active': editor.isActive('blockquote') }">
                Цитата
              </n-button>
              <h3>Форматирование</h3>
              <n-button @click="editor.chain().focus().setHorizontalRule().run()">
                Разделить страницу
              </n-button>
              <n-button @click="editor.chain().focus().setHardBreak().run()">
                Перенос строки
              </n-button>
              <h3>Отмена и отмена отмены</h3>
              <n-button @click="editor.chain().focus().undo().run()">
                Отменить
              </n-button>
              <n-button @click="editor.chain().focus().redo().run()">
                Отменить отмену
              </n-button>
              <h3>Работа с таблицами</h3>
              <n-button @click="editor.chain().focus().insertTable({ rows: 3, cols: 3, withHeaderRow: true }).run()">
                Вставить таблицу
              </n-button>
              <n-button @click="editor.chain().focus().addColumnBefore().run()" :disabled="!editor.can().addColumnBefore()">
                Добавить столбец до
              </n-button>
              <n-button @click="editor.chain().focus().addColumnAfter().run()" :disabled="!editor.can().addColumnAfter()">
                Добавить столбец после
              </n-button>
              <n-button @click="editor.chain().focus().deleteColumn().run()" :disabled="!editor.can().deleteColumn()">
                Удалить столбец
              </n-button>
              <n-button @click="editor.chain().focus().addRowBefore().run()" :disabled="!editor.can().addRowBefore()">
                Добавить строку до
              </n-button>
              <n-button @click="editor.chain().focus().addRowAfter().run()" :disabled="!editor.can().addRowAfter()">
                Добавить строку после
              </n-button>
              <n-button @click="editor.chain().focus().deleteRow().run()" :disabled="!editor.can().deleteRow()">
                Удалить строку
              </n-button>
              <n-button @click="editor.chain().focus().deleteTable().run()" :disabled="!editor.can().deleteTable()">
                Удалить таблицу
              </n-button>
              <n-button @click="editor.chain().focus().toggleHeaderColumn().run()" :disabled="!editor.can().toggleHeaderColumn()">
                Выделить столбец
              </n-button>
              <n-button @click="editor.chain().focus().toggleHeaderRow().run()" :disabled="!editor.can().toggleHeaderRow()">
                Выделить строку
              </n-button>
              <n-button @click="editor.chain().focus().toggleHeaderCell().run()" :disabled="!editor.can().toggleHeaderCell()">
                Выделить ячейку
              </n-button>
              <n-button @click="editor.chain().focus().mergeOrSplit().run()" :disabled="!editor.can().mergeOrSplit()">
                Объединить/разъединить ячейки
              </n-button>
            </n-space>
          </n-layout-sider>
          <n-layout-content content-style="padding: 24px;">
            <editor-content :editor="editor" />
          </n-layout-content>
        </n-layout>
      </n-tab-pane>
      <n-tab-pane name="settings" tab="Настройки">
        <n-layout>
        <n-space horizontal justify="space-evenly">
          <n-card>
            <h2>Название статьи</h2><n-input v-model:value="value" type="text" placeholder= {{article.name}} />
            <h2>Категория</h2><n-select v-model:value="value" :options="categoriesNames"></n-select>
          </n-card>
          <n-card>
            <h2>Загрузить обложку</h2>
            <n-upload directory-dnd action="" :max="1">
              <n-upload-dragger>
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
          <n-card>
            <h3>Автор</h3>
            <n-input v-model:value="value" type="text" placeholder="Алена Изотова" />
            <h3>Дизайнер</h3>
            <n-input v-model:value="value" type="text" placeholder="Ольга Бартель" />
            <h3>Редактор</h3>
            <n-input v-model:value="value" type="text" placeholder="Евгений Козило" />
          </n-card>
          <n-card>
            <n-space vertical>
              <h3>Отложить статью</h3>
              <n-input-group>
                <n-date-picker />
                <n-time-picker />
              </n-input-group>
              <n-space horizontal>
                <n-button type="warning">Сохранить</n-button>
                <n-button type="primary">Опубликовать сейчас</n-button>
              </n-space>
              <n-button type="error">Удалить</n-button>
            </n-space>
          </n-card>
        </n-space>
        </n-layout>
      </n-tab-pane>
    </n-tabs>
  </n-layout>
</template>

<script>
import { Editor, EditorContent, BubbleMenu, FloatingMenu } from '@tiptap/vue-3'
import Table from '@tiptap/extension-table'
import TableCell from '@tiptap/extension-table-cell'
import TableHeader from '@tiptap/extension-table-header'
import TableRow from '@tiptap/extension-table-row'
import StarterKit from '@tiptap/starter-kit'
import api from '../../stores/api.js'
import {NButton, NLayout, NTabPane, NTabs, NSpace, NInput, NCard, NSelect, useMessage,
  NUpload, NUploadDragger, NInputGroup, NDatePicker, NTimePicker, NLayoutSider, NMenu, NLayoutContent} from 'naive-ui'
import useTokenStore from "~/stores/modules/token";
import useArticleStore from "~/stores/modules/article";
import {ref} from "vue";

const CustomTableCell = TableCell.extend({
  addAttributes() {
    return {
      ...this.parent?.(),

      backgroundColor: {
        default: null,
        parseHTML: element => element.getAttribute('data-background-color'),
        renderHTML: attributes => {
          return {
            'data-background-color': attributes.backgroundColor,
            style: `background-color: ${attributes.backgroundColor}`,
          }
        },
      },
    }
  },
})

export default {
  components: {
    EditorContent, NLayout, NTabs, NTabPane, NSpace, NInput, NCard, NSelect, NUpload, NUploadDragger, NButton,
    NInputGroup, NDatePicker, NTimePicker, NLayoutSider, NMenu, NLayoutContent, BubbleMenu, FloatingMenu
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
        Table.configure({
          resizable: true,
        }),
        TableRow,
        TableHeader,
        // Default TableCell
        // TableCell,
        // Custom TableCell with backgroundColor attribute
        CustomTableCell,
      ],
    })
  },

  beforeDestroy() {
    this.editor.destroy()
  },
}
</script>

<style scoped>
  .n-card {
    height: 100%;
  }
</style>

<style lang="scss">
.bubble-menu {
  display: flex;
  background-color: #0D0D0D;
  padding: 0.2rem;
  border-radius: 0.5rem;

  button {
    border: none;
    background: none;
    color: #FFF;
    font-size: 0.85rem;
    font-weight: 500;
    padding: 0 0.2rem;
    opacity: 0.6;

    &:hover,
    &.is-active {
      opacity: 1;
    }
  }
}

.floating-menu {
  display: flex;
  background-color: #0D0D0D10;
  padding: 0.2rem;
  border-radius: 0.5rem;

  button {
    border: none;
    background: none;
    font-size: 0.85rem;
    font-weight: 500;
    padding: 0 0.2rem;
    opacity: 0.6;

    &:hover,
    &.is-active {
      opacity: 1;
    }
  }
}
.ProseMirror {
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 100%;
    margin: 0;
    overflow: hidden;

    td,
    th {
      min-width: 1em;
      border: 2px solid #ced4da;
      padding: 3px 5px;
      vertical-align: top;
      box-sizing: border-box;
      position: relative;

      > * {
        margin-bottom: 0;
      }
    }

    th {
      font-weight: bold;
      text-align: left;
      background-color: #f1f3f5;
    }

    .selectedCell:after {
      z-index: 2;
      position: absolute;
      content: "";
      left: 0; right: 0; top: 0; bottom: 0;
      background: rgba(200, 200, 255, 0.4);
      pointer-events: none;
    }

    .column-resize-handle {
      position: absolute;
      right: -2px;
      top: 0;
      bottom: -2px;
      width: 4px;
      background-color: #adf;
      pointer-events: none;
    }

    p {
      margin: 0;
    }
  }
}

.tableWrapper {
  overflow-x: auto;
}

.resize-cursor {
  cursor: ew-resize;
  cursor: col-resize;
}
</style>