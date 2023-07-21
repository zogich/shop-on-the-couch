<template>
  <editor-content :editor="editor" />
  {{article}}
</template>

<script>
import { Editor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import api from '../../stores/api.js'

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
    this.editor = new Editor({
      content: '<p>I’m running Tiptap with Vue.js. 🎉</p>',
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