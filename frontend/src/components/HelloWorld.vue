<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Một hệ thống quản lý đăng kiểm cho xe ô tô</h2>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* Add a sans-serif font for the body text */
/* Add some color and style to the headings */
.hello h1, .hello h2 {
  color: #333;
  text-align: center;
  margin-bottom: 20px;
}

/* Add some style to the body text */
.hello p {
  color: #555;
  font-size: 18px;
  text-align: justify;
}

/* Add some style to links */
.hello a {
  color: #42b983;
  text-decoration: none;
}

.hello a:hover {
  text-decoration: underline;
}

/* Add some style to buttons */
.hello button {
  background-color: #42b983;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.hello button:hover {
  background-color: #2a9d8f;
}


</style>
