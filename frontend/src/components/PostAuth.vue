<template>
    <Sidebar />
    <div :style="{ 'margin-left': sidebarWidth }">
        <router-view />
    </div>
</template>

<script>
    import Sidebar from '@/components/sidebar/SideBar'
    import { sidebarWidth } from '@/components/sidebar/state'

    export default {
        name: 'PostAuth',
        components: {
            Sidebar,
        },
        setup() {
          return { sidebarWidth }
        }
    }
</script>
<style lang="scss" scoped>
  #appli {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #navi {
    padding: 30px;
  }
  
  #navi a {
    font-weight: bold;
    color: #2c3e50;
  }
  
  #navi a.router-link-exact-active {
    color: #42b983;
  }
</style>