<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1 style="text-align: center;">
      <span v-if="collapsed">
        <div>R</div>
        <div>T</div>
      </span>
      <span v-else>Registry Total</span>
    </h1>

    <SidebarLink to="/" icon="fas fa-home">Home</SidebarLink>
    <SidebarLink to="/dashboard" icon="fas fa-columns">Dashboard</SidebarLink>
    <SidebarLink to="/analytics" icon="fas fa-chart-bar">Analytics</SidebarLink>
    <SidebarLink to="/register" icon="fas fa-registered" v-if="isSuperuser">Create Account</SidebarLink>
    <SidebarLink to="" icon="fas fa-sign-out" @click="logout">Logout</SidebarLink>
    <span class="user">{{username}}</span>
    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<script>
import axios from 'axios'
import SidebarLink from './SidebarLink'
import { collapsed, toggleSidebar, sidebarWidth } from './state'
import index from '../../store/index'

export default {
  components: { SidebarLink },
  setup() {
    return { collapsed, toggleSidebar, sidebarWidth }
  },
  data() {
    return {
      isSuperuser: false,
    }
  },
  computed: {
    username: function() {
        return index.getters.getUsername;
      },
  },
  methods: {
    async logout() {
    await axios
      .post('/api/v1/token/logout/')
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
          console.log(JSON.stringify(error))
      })
        
      axios.defaults.headers.common['Authorization'] = ''
      this.$store.commit('removeToken')

      this.$router.push('/')
    },
    async checkSuperuser() {
      try {
        const response = await axios.get('/api/check_superuser/')
        this.isSuperuser = response.data.is_superuser
      } catch (error) {
        console.log(error.response)
      }
    },
  },
  async mounted() {
    try {
      const token = localStorage.getItem('token')
      if (token) {
        axios.defaults.headers.common['Authorization'] = `Token ${token}`
        await this.checkSuperuser()
      } else {
        this.$router.push('/') // Redirect to login if token is not available
      }
    } catch (error) {
      console.log(error)
    }
  },
}
</script>

<style>
:root {
  --sidebar-bg-color: #2f855a;
  --sidebar-item-hover: #38a169;
  --sidebar-item-active: #276749;
}
</style>

<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);

  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;

  transition: 0.3s ease;

  display: flex;
  flex-direction: column;
}

.sidebar h1 {
  height: 2.5em;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;

  color: rgba(255, 255, 255, 0.7);

  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}

.user {
  position: absolute;
  bottom: 2.5em;
  left: 50%;
  transform: translateX(-50%);
  font-weight: bold;
  font-size: 1.2em;
}
</style>