<template>
  <nav>
    <component :is="navComponent"></component>
  </nav>
</template>

<script>
  import PreAuth from '@/components/PreAuth'
  import PostAuth from '@/components/PostAuth'
  import axios from 'axios'

  export default {
    name: 'App',
    components: {
      PreAuth,
      PostAuth
    },
    computed: {
      navComponent() {
        return this.$store.state.token ? PostAuth : PreAuth
      }
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      if (this.$store.state.token) {
          axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
      } else {
          axios.defaults.headers.common['Authorization'] = ""
      }
    }
  }
</script>