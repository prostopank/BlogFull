import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import store from './store'
import router from './router'

require('@/store/subscribe')



axios.defaults.baseURL ='http://127.0.0.1:8000/api'

Vue.config.productionTip = false

store.dispatch('auth/attempt', localStorage.getItem('token'))

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
