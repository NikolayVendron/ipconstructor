import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Главная',
    component: Home
  },
  {
    path: '/reviews',
    name: 'Отзывы',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Reviews.vue')
  },
  {
    path: '/about',
    name: 'О нас',
    component: () => import('../views/About.vue')
  },
  {
    path: '/create',
    name: 'Создать альбом',
    component: () => import('../views/Create.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
