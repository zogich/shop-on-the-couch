<template>
  <n-layout>
    <n-space vertical size="large">
      <n-h1>
        <n-text>Авторизация</n-text>
      </n-h1>
          <n-space vertical>
            <n-input v-model:value="username" placeholder="username" />
            <n-input v-model:value="password" placeholder="password" type="password" show-password-on="mousedown" />
            <n-space justify="end">
              <n-button @click='login'>Login</n-button>
              <n-button @click="logout">Logout</n-button>
            </n-space>
          </n-space>
      Авторизация:
      {{this.$store.state.token.isAuthenticated}}
    </n-space>
  </n-layout>
</template>

<script>

import { NButton, NInput, NSpace, NH1, NText, NLayout } from 'naive-ui'

export default {
  name: "LoginView",
  components: {
    NButton, NInput, NSpace, NH1, NText, NLayout
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