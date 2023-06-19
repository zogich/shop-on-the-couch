<script setup>
import ArticleCardNormal from "../components/ArticleCardNormal.vue";
import ArticleCardLong from "../components/ArticleCardLong.vue";
</script>

<template>
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
    <n-grid cols="1 s:2 m:4" responsive="screen" :x-gap="10" :y-gap="10">
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
      <n-grid-item><ArticleCardNormal/></n-grid-item>
    </n-grid>
</template>

<script>
import {NButton, NLayout, NSpace, NCard, NGrid, NGridItem, NBackTop} from 'naive-ui'

export default {
  name: "HomeView",
  components: {
    NLayout, NButton, NSpace, NCard, NGrid, NGridItem, NBackTop
  }
}
</script>

<style scoped>

</style>