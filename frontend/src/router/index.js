import { createRouter, createWebHistory } from 'vue-router'
import HomeView from "../views/HomeView.vue";
import ArticleView from "../views/ArticleView.vue";
import LoginView from "../views/LoginView.vue";
import MagazineAdminView from "../views/MagazineAdminView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView
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
    {
      path: '/magazine-admin',
      name: 'magazine-admin',
      component: MagazineAdminView
    }
  ]
})

export default router
