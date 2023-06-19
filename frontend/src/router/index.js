import { createRouter, createWebHistory } from 'vue-router'
import CatalogView from "../views/CatalogView.vue";
// <<<<<<< Updated upstream
import HomeView from "../views/HomeView.vue";
// =======
import ArticleView from "../views/ArticleView.vue";
// >>>>>>> Stashed changes

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: CatalogView
    },
    {
      path: '/',
      name: '',
      component: HomeView
    },
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
  ]
})

export default router
