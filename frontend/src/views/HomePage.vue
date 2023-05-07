<template>
  <div class="custom">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Registry Total" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomePage',
  components: {
    HelloWorld
  }
}
</script>

<style scoped>
  .custom {
    text-align: center;
  }
</style>