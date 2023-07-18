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
      <n-grid-item v-for="item in this.$store.state.article.articles" :key="item.id" >
        <router-link :to="{ name: 'article', params: {id: item.id} }"><ArticleCardNormal :article="item"></ArticleCardNormal></router-link>
      </n-grid-item>
    </n-grid>
  </n-layout>
</template>

<script>
import { NLayout, NGrid, NGridItem, NBackTop } from 'naive-ui'
import ArticleCardNormal from "../components/ArticleCardNormal.vue";
import ArticleCardLong from "../components/ArticleCardLong.vue";


export default {
  name: "HomeView",
  components: {
    NLayout, NGrid, NGridItem, NBackTop, ArticleCardNormal, ArticleCardLong
  },
  data(){
    return {
      articles: [],
    }
  },
  methods: {
  },

}
</script>

<style scoped>

</style>