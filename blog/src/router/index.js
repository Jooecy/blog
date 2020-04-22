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
    redirect: '/search',

    },
  {
    path: '/search',
    component: Search,
    meta: {
      keepAlive: true
    }
  },
  {
    path: '/blog',
    component: Blog,
    meta: {
      keepAlive: true
    }
  },
  {
    path: '/marks',
    component: Marks,
    meta: {
      keepAlive: true
    }
  },
  {
    path: '/about',
    component: About,
    meta: {
      keepAlive: true
    }
  },
  {
    path: '/info',
    component: Info,
    meta: {
      keepAlive: true
    }
  },
]

const router = new VueRouter({
  routes,
  // mode:'history'
})


export default router
