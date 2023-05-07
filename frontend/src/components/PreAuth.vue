<template>
  <div>
    <Navbar />
    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
          <div class="lds-dual-ring"></div>
      </div>

    <section class="section">
        <router-view/>
    </section>
  </div>
</template>

<script>
  import Navbar from '@/components/NavBar'

  export default {
      name: 'PreAuth',
      components: {
          Navbar
      }
  }   
</script>