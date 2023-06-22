<template>
  <n-layout>
    <n-card title="Название статьи" size="large">
      <template #cover>
      </template>
      <div class="date-and-category">
        <span>01.01.2001</span>
        <span>Категория</span>
      </div>
    </n-card>
  </n-layout>
</template>

<script>

import {NCard, NLayout, NSpace, NButton} from 'naive-ui'

export default {
  name: "ArticleCardNormal",
  components: {
    NCard, NLayout, NSpace, NButton
  }
}

</script>

<style scoped>

.n-card {
  width: 100%;
  border-radius: 7px;
}

.n-layout {
  padding: 0 0 10px 0;
}

.date-and-category {
  display: flex;
}

.date-and-category > span {
  margin-right: 10px;
}

</style>