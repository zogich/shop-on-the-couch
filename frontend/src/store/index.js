import { createStore } from 'vuex'
import articleModule from "./modules/article.js";

export default createStore({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    article: articleModule,
  },
})