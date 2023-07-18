
<!--Зарегистрированным пользователям можно делать push-рассылку на почту-->
<!--рабоатет только для тех, кто дал согласие-->

<template>
  <n-layout>
    <n-space vertical size="large">
      <n-h1>
        <n-text>Авторизация</n-text>
      </n-h1>
          <n-space vertical>
            <n-input v-model:value="usrnm" placeholder="username" />
            <n-input v-model:value="psswrd" placeholder="password" type="password" show-password-on="mousedown" />
            <n-space justify="end">
              <n-button @click='login'>Login</n-button>
              <n-button @click="logout">Logout</n-button>
            </n-space>
          </n-space>
      Авторизация:
      {{ tokenStore.isAuthenticated }}
    </n-space>
  </n-layout>
</template>

<script setup>

  import useTokenStore from "../stores/modules/token";

  let usrnm = ref('');
  let psswrd = ref('');
  const tokenStore = useTokenStore()

  async function login(){
      await tokenStore.login({username: usrnm.value, password: psswrd.value})
  }

  async function logout(){
    await tokenStore.logout()
  }
</script>

<script>

import { NButton, NInput, NSpace, NH1, NText, NLayout } from 'naive-ui';

export default {
  name: "LoginView",
  components: {
    NButton, NInput, NSpace, NH1, NText, NLayout
  },

}
</script>

<style scoped>
</style>