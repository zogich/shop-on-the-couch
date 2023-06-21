import { createRouter, createWebHistory } from 'vue-router'
import HomeView from "../views/HomeView.vue";
import ArticleView from "../views/ArticleView.vue";
import LoginView from "../views/LoginView.vue";

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
      component: LoginView
    },
    {
      path: '/',
      name: '',
      component: HomeView
    },
    {
      path: '/article/:id/',
      name: 'article',
      component: ArticleView,
      props: (route) =>{
        const articleId = route.params.id;
        return { articleId, ...route.params }
      }
    },
  ]
})

export default router
