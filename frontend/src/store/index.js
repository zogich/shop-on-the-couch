import { createStore } from 'vuex'
import articleModule from "./modules/article.js";
import tokenModule from "./modules/token";

export default createStore({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    article: articleModule,
    token: tokenModule,
  },
})