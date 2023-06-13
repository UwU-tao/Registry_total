<template>
    <div class="navbar">
        <router-link to="/" v-bind:class="{ active: activeLink === '/' }" @click="activeLink = '/'">Home</router-link>
        <router-link to="/about" v-bind:class="{ active: activeLink === '/about' }" @click="activeLink = '/about'">About</router-link>
        <router-link to="/login" v-bind:class="{ active: activeLink === '/login' }" @click="activeLink = '/login'">Login</router-link>
    </div>
</template>

<script>
    export default {
        name: 'NavBar',
        data() {
            return {
                activeLink: '/'
            }
        },
    }
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  background-color: #333;
  font-family: Arial, Helvetica, sans-serif;
}

.navbar a {
  color: white;
  text-decoration: none;
  font-size: 17px;
  padding: 14px 16px;
}

.navbar a:hover {
  background-color: #ddd;
  color: black;
}

.navbar a.active {
  background-color: #04AA6D;
  color: white;
}

@media (max-width: 600px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
    padding: 10px;
  }

  .navbar a {
    display: block;
    width: 100%;
    text-align: left;
    padding: 10px;
    margin-bottom: 5px;
    border-bottom: 1px solid #ddd;
  }
}

</style>