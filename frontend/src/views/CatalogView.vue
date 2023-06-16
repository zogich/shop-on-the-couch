<template>
  <div>
    Ваше имя: {{name}}
    Это будущий каталог.
    <n-button>Ок</n-button>
  </div>
</template>

<script>

import {NButton} from 'naive-ui'

export default {
  name: "CatalogView",
  components: {
    NButton
  },
  data(){
    return {
      name: 'Егор',
    }
  }
}
</script>

<style scoped>

</style>