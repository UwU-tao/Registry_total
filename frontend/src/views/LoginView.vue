<template>
    <div class="login-view">
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" class="form-control" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" class="form-control" id="password" v-model="password" required>
      </div>
      <button type="submit" class="btn btn-primary">Log in</button>
    </form>
  </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'LoginView',
        data() {
            return {
                username: '',
                password: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')

                const formData = {
                    username: this.username,
                    password: this.password
                }

                await axios
                    .post('/api/v1/token/login/', formData)
                    .then(response => {
                        const token = response.data.auth_token

                        this.$store.commit('setToken', token)

                        axios.defaults.headers.common['Authorization'] = 'Token ' + token

                        localStorage.setItem('token', token)

                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                    })

                await axios
                    .get('/api/v1/users/me') //default from djoser
                    .then(response => {
                        this.$store.commit('setUser', {'id': response.data.id, 'username': response.data.username})

                        localStorage.setItem('username', response.data.username)

                        localStorage.setItem('userid', response.data.id)

                        this.$router.push('/dashboard')
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>

<style scoped>
.login-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90vh;
  background-color: #f5f5f5;
}

form {
  background-color: #fff;
  padding: 30px;
  border-radius: 5px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
}

.form-group {
  margin-bottom: 20px;
}

label {
  font-weight: bold;
}

input[type="text"],
input[type="password"] {
  border: none;
  border-bottom: 1px solid #ccc;
  padding: 10px;
  width: 100%;
  font-size: 16px;
}

button[type="submit"] {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button[type="submit"]:hover {
  background-color: #0069d9;
}
</style>