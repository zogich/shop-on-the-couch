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
    <n-grid cols="1 s:2 m:4" responsive="screen" :x-gap="10" :y-gap="10">
      <n-grid-item v-for="item in articleStore.getAllArticles" :key="item.id" >
        <NuxtLink :to="{ name: 'article-id', params: {id: item.id}} ">
          <ArticleCardNormal :article="item"></ArticleCardNormal>
        </NuxtLink>
      </n-grid-item>
    </n-grid>
  </n-layout>
</template>

<script setup>
  import useArticleStore from "../stores/modules/article";
  import useTokenStore from "../stores/modules/token";
  const tokenStore = useTokenStore();
  const articleStore = useArticleStore();
</script>

<script>
import {NButton ,NLayout, NGrid, NGridItem, NBackTop } from 'naive-ui'
import ArticleCardNormal from '../components/ArticleCardNormal'
import ArticleCardLong from '../components/ArticleCardLong'

export default {
  name: "HomeView",
  components: {
    NLayout, NGrid, NGridItem, NBackTop, NButton, ArticleCardNormal, ArticleCardLong
  },

  async created(){
  }
}


</script>
