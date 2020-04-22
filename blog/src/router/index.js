import Vue from 'vue'
import VueRouter from 'vue-router'
import Search from 'components/search/Search'

const Blog = () => import('components/blog/Blog')
const Login = () => import('components/Login')
const Marks = () => import('components/marks/Marks')
const About = () => import('components/about/About')
const Info = () => import('components/info/Info')
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
  },
  {
    path: '/marks',
    component: Marks
  },
  {
    path: '/about',
    component: About
  },
  {
    path: '/info',
    component: Info
  },
]

const router = new VueRouter({
  routes,
  // mode:'history'
})


export default router
