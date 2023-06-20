<script setup>
import ArticleCardNormal from "../components/ArticleCardNormal.vue";
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
  <n-image src="../src/assets/logo.svg"/>
  <div class="article-header">
    <n-h1>
      <n-text>Название статьи</n-text>
    </n-h1>
    <n-text itelic style="margin-right: 10px">01.01.2021</n-text>
    <n-text type="info">Категория</n-text>
  </div>
  <n-divider/>
  <div class="article-content">
<!--    <p>{{this.article.text}}}</p>-->
    <p>Здесь должен быть текст статьи</p>
  </div>
  <n-grid cols="1 s:2 m:3" responsive="screen" :x-gap="10" :y-gap="10">
    <n-grid-item>
      <ArticleCardNormal></ArticleCardNormal>
    </n-grid-item>
    <n-grid-item>
      <ArticleCardNormal></ArticleCardNormal>
    </n-grid-item>
    <n-grid-item>
      <ArticleCardNormal></ArticleCardNormal>
    </n-grid-item>
  </n-grid>
  <n-h1>
    <n-text>Читайте также:</n-text>
  </n-h1>
</template>

<script>
import {NButton, NLayout, NSpace, NBackTop, NLayoutContent, NH1, NText, NImage, NDivider, NGrid} from 'naive-ui'
// import ArticleCardNormal from "../components/ArticleCardNormal.vue";

export default {
  name: "ArticleView",
  components: {
    NLayout, NButton, NSpace, NBackTop, NLayoutContent, NH1, NText, NImage, NDivider, NGrid
  },
  props: {
    article: Object
  },
  async created(){
    console.log(this.article)
  }
}
</script>

<style scoped>
  .article-header >.n-h1 > .n-text{
    font-size: 2.5rem;
  }
  .article-header > .n-text {
    font-size: 1.125rem;
  }
  .article-content {
    border: rgb(239, 239, 245) solid 1px;
    border-radius: 5px;
    padding: 10px;
  }
</style>