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
  <n-image src="../src/assets/logo.svg"/>
    <nuxt-link :to="{ name: 'editor-id', params:{id: article.id}} "><n-button></n-button></nuxt-link>
  <div class="article-header">
    <n-h1>
      <n-text>{{article.name}}</n-text>
    </n-h1>
    <n-text itelic style="margin-right: 10px">{{article.date}}</n-text>
    <n-text type="info">{{article.category}}</n-text>
  </div>
  <n-divider/>
  <div class="article-content">
   <p>{{article.text}}</p>
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
  </n-layout>
</template>

<script>
import {NButton, NLayout, NSpace, NBackTop, NLayoutContent, NH1, NText, NImage, NDivider, NGrid} from 'naive-ui'
import ArticleCardNormal from "../../components/ArticleCardNormal.vue";
import api from '../../stores/api.js'

export default {
  name: "ArticleView",
  components: {
    NLayout, NButton, NSpace, NBackTop, NLayoutContent, NH1, NText, NImage, NDivider, NGrid, ArticleCardNormal
  },
  props: {
    articleId: 0
  },

  async setup(){
    const route = useRoute();
    let article = null;
    await api.get('/api/article/', {params: { id: route.params.id }}).then(response =>{
      article = response.data[0]
    })
    return { route, article }
  },

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