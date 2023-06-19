<template>
  <div>
    <n-button type="error">Ок</n-button>
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
      name: 'Михаил',
    }
  }
}
</script>

<style scoped>

</style>