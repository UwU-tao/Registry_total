<template>
    <div class="navbar">
        <router-link to="/" class="active">Home</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/login">Login</router-link>
    </div>
</template>

<script>
    export default {
        name: 'NavBar'
    }
</script>

<style scoped>
.navbar {
overflow: hidden;
background-color: #333;
margin: 0;
font-family: Arial, Helvetica, sans-serif;
}

.navbar a {
float: left;
display: block;
color: white;
text-align: center;
padding: 14px 16px;
text-decoration: none;
font-size: 17px;
}

.navbar a:hover {
background-color: #ddd;
color: black;
}

.navbar a.active {
background-color: #04AA6D;
color: white;
}
</style>