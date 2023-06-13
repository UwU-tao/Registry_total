<template>
  <div class="registration-form">
    <h2>Center List</h2>
    <button @click="openModal">Register</button>
    <div class="modal" :class="{ 'show': showModal }">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h1>Register</h1>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" v-model="username" required>
          </div>
          <div class="form-group">
            <label for="password1">Password</label>
            <input type="password" id="password1" v-model="password1" required>
          </div>
          <div class="form-group">
            <label for="password2">Confirm Password</label>
            <input type="password" id="password2" v-model="password2" required>
          </div>
          <div class="error" v-if="errors.length">
            <ul>
              <li v-for="error in errors" :key="error">{{ error }}</li>
            </ul>
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
    <CenterTable/>
  </div>
</template>

<script>
import axios from 'axios'
import CenterTable from '@/components/CenterTable.vue'

export default {
  name: 'SignupView',
  components: {
    CenterTable,
  },
  data() {
    return {
      username: '',
      password1: '',
      password2: '',
      errors: [],
      showModal: false
    }
  },
  methods: {
    async submitForm() {
      this.errors = []

      if (!this.username) {
        this.errors.push('Username is required.')
      }

      if (!this.password1) {
        this.errors.push('Password is required.')
      }

      if (this.password1 !== this.password2) {
        this.errors.push('Passwords do not match.')
      }

      if (this.errors.length === 0) {
        try {
          const formData = {
            username: this.username,
            password: this.password1
          }

          const response = await axios.post('/api/v1/users/', formData)
          console.log(response.data)
          // this.$router.push('/login')
        } catch (error) {
          if (error.response && error.response.data) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else {
            this.errors.push('Something went wrong. Please try again!')
          }
        }
      }
    },
    openModal() {
      this.showModal = true
    },
    closeModal() {
      this.showModal = false
    }
  }
}
</script>

<style scoped>
.registration-form {
  text-align: center;
}

.modal {
  display: none;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal.show {
  display: block;
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #555555;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border-radius: 3px;
  border: 1px solid #cccccc;
  font-size: 16px;
}

textarea {
  height: 100px;
}

button[type="submit"] {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  border: none;
  color: #ffffff;
  font-size: 16px;
  border-radius: 3px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #45a049;
}

.error {
  color: red;
  margin-bottom: 10px;
}
</style>
