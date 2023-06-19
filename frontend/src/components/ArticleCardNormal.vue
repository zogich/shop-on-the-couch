<template>
  <n-layout>
  <n-card title="Название статьи" size="medium">
    <template #cover>
      <img src="./src/assets/logo.svg" alt="">
    </template>
    <p class="card-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    <n-divider />
    <div class="date-and-category">
      <span>01.01.2001</span>
      <span>Категория</span>
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
  }
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