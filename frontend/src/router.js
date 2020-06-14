import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // Lazi loading routes
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/auth/login',
      component: () => import(/* webpackChunkName: "login" */ './views/Login.vue')
    },
    {
      path: '/auth/sign-up',
      component: () => import(/* webpackChunkName: "sign-up" */ './views/Signup.vue')
    },
    {
      path: '/strip',
      component: () => import(/* webpackChunkName: "strip" */ './views/Strip.vue')
    },
    {
      path: '/htn',
      component: () => import(/* webpackChunkName: "htn" */ './views/Htn.vue')
    },
    {
      path: '/dashboard',
      component: () => import(/* webpackChunkName: "dashboard" */ './views/Dashboard.vue')
    }
  ]
})
