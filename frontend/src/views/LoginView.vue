<template>
  <div>
    <input v-model="username" placeholder="username">
    <input v-model="password" placeholder="password">
    <button @click='login'>Login</button>
    <button @click="logout">Logout</button>
    Авторизация:
    {{this.$store.state.token.isAuthenticated}}
  </div>
</template>

<script>

import {NButton} from 'naive-ui'
import api from "../store/api";

export default {
  name: "LoginView",
  components: {
    NButton
  },
  data(){
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    async login(){
      this.$store.dispatch('login', {username: this.username, password: this.password});
      console.log(this.$store.state.token.userData)
    },
    async logout(){
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style scoped>

</style>