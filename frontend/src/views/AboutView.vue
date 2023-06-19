<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
  <n-button @click="this.test"></n-button>
</template>


<script>
import {NButton} from 'naive-ui'

export default {
  components: {
    NButton
  },
  methods:{
    async test(){
      await this.$store.dispatch('fetchCategories');
      // console.log(this.$store.state.catalog.categories[0].name)
    }
  }
}

</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
