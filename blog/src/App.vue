<template>
  <div id="app">
    <!-- <button @click="yz">验证</button>
    {{loginStatus}} -->
    <nav-bar></nav-bar>
    
    <router-view></router-view>
    <div class="hidden-sm-and-up"><mobile-nav></mobile-nav></div>
    
  </div>
</template>

<script>

import NavBar from 'components/navbar/NavBar'
import MobileNav from 'components/mobile/MobileNav'
import {request} from './network/request'
export default {
  name: 'app',
  data() {
    return {
      loginStatus: false
    }
  },
  components: {
    NavBar,
    MobileNav
  },
  watch: {
    $route(to){
      this.getStatus()
    }
  },
  methods: {
    yz() {
      request({
           url: '/api/do_something/',
           method: 'post',
           headers: {'Authorization':localStorage.getItem('logintoken')}

            
          }).then(res => {
            //  console.log(res);
             }
          )
    },
    delStatus() {
      localStorage.removeItem('logintoken')
      window.location.reload()
    },
    getStatus(){
      const token = localStorage.getItem('logintoken')
      // console.log(token);  
      
      if(token){
        this.$store.commit('changeLoginStatus')
      }
      this.loginStatus = this.$store.getters.getStatus
    }
    
  },
}
</script>

<style>

</style>
