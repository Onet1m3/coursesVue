import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    meta: { layout: 'main' },
    component: () => import('../views/Home')
  },
  {
    path: '/school/:slug',
    name: 'School',
    meta: { layout: 'main' },
    component: () => import('../views/DetailSchool'),
    props: true
  },
  {
    path: '/course/:slug',
    name: 'CategoriesCourses',
    meta: { layout: 'main' },
    component: () => import('../components/app/sidebar/ListCategoriesCourses'),
    props: true
  },
  {
    path: '/login',
    name: 'Login',
    meta: { layout: 'auth' },
    component: () => import('../views/Login')
  },
  {
    path: '/register',
    name: 'Register',
    meta: { layout: 'auth' },
    component: () => import('../views/Register')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
