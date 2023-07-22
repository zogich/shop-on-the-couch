<template>
  <editor-content :editor="editor" />
</template>

<script>
import { Editor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import api from '../../stores/api.js'
import article from "~/stores/modules/article";

export default {
  components: {
    EditorContent,
  },

  data() {
    return {
      editor: null,
    }
  },

  async setup(){
    const route = useRoute()
    let article = null;
    await api.get('/api/article/', {params: { id: route.params.id }}).then(response =>{
      article = response.data[0]
    })
    return {route, article}
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