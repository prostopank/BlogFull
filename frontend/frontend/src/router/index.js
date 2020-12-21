import Vue from 'vue'
import VueRouter from 'vue-router'

import SignIn from '../components/SignIn'
Vue.use(VueRouter)

const routes = [
    {
        path: '/signIn',
        name: 'signIn',
        component: SignIn
    }

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router