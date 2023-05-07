import { createRouter, createWebHistory } from "vue-router"
import Home from '../views/HomePage.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('../views/DashBoard.vue'),
    meta: {requireLogin: true}
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/AboutPage.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
