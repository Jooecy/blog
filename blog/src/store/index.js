import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    loginStatus: false
  },
  getters: {
    getStatus(state) {
      // if(state.loginStatus){
        return state.loginStatus
      // }else{
      //   this.$store.commit('changeLoginStatus')
      // }
      
    }
  },
  mutations: {
    changeLoginStatus(state) {
      state.loginStatus = true
    }
  },
  actions: {
  },
  modules: {
  }
})

export default store