<template>
  <n-layout>
  <n-back-top
      :right="40"
      :bottom="160"
      :style="{
      transition: 'all .3s cubic-bezier(.4, 0, .2, 1)'
    }"
  >
    <div
        style="
        width: 200px;
        height: 40px;
        line-height: 40px;
        text-align: center;
        font-size: 14px;
      "
    >
      Вверх
    </div>
  </n-back-top>
  <ArticleCardLong />
  </n-layout>

</template>

<script>
import {NButton ,NLayout, NGrid, NGridItem, NBackTop } from 'naive-ui'

export default {
  name: "HomeView",
  components: {
    NLayout, NGrid, NGridItem, NBackTop, NButton
  },
  data() {
    return {
      articles: [],
    }
  }
}

</script>