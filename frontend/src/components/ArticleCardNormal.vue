<template>
  <n-layout>
  <n-card :title="this.article.name" size="medium">
    <template #cover>
    </template>
    <p class="card-description"> {{this.article.text}} </p>
    <n-divider />
    <div class="date-and-category">
      <span>01.01.2001</span>
      <span>{{this.article.category}}</span>
    </div>
  </n-card>
  </n-layout>
</template>

<script>

import {NCard, NLayout, NSpace, NButton, NDivider} from 'naive-ui'

export default {
  name: "ArticleCardNormal",
  components: {
    NCard, NLayout, NSpace, NButton, NDivider
  },
  props: {
    article: Object
  },
  async created(){
  },
}

</script>

<style scoped>

.n-card {
  border-radius: 7px;
}

.date-and-category {
  display: flex;
  justify-content: space-between;
}

.card-description{
  -ms-text-overflow: ellipsis;
  text-overflow: ellipsis;
  overflow: hidden;
  -webkit-line-clamp: 5;
  display: -webkit-box;
  word-wrap: break-word;
  -webkit-box-orient: vertical;
  box-orient: vertical;
  line-height: 19px;
}

</style>