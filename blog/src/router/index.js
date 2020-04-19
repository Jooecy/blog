import Vue from 'vue'
import VueRouter from 'vue-router'
import Search from 'components/search/Search'

const Blog = () => import('components/blog/Blog')
const Login = () => import('components/Login')
Vue.use(VueRouter)

  const routes = [
    {
    path: '/login',
    component: Login,
    },
    {
    path: '',
    redirect: '/search'
    },
  {
    path: '/search',
    component: Search,
  },
  {
    path: '/blog',
    component: Blog
  }
]

const router = new VueRouter({
  routes,
  // mode:'history'
})


export default router
