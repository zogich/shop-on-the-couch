import './assets/main.css'
import store from './store/index'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router).use(store)

app.mount('#app')
