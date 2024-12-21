import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Main from '@/components/Main.vue'
import Login from '@/components/Login.vue'
import Register from '@/components/Register.vue'
import PersonalAccount from '@/components/PersonalAccount.vue'
import Profile from '@/components/Profile.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Main,
    },
    {path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/l',
      name: 'PersonalAccount',
      component: PersonalAccount
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    }
  ],
})

export default router
