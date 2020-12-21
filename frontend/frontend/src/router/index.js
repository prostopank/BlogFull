import Vue from 'vue'
import VueRouter from 'vue-router'

import SignIn from '../views/SignIn.vue'
import Registration from '../views/Registration.vue'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/SignIn',
        component: SignIn
    },
    {
        path: '/Registration',
        component: Registration
    }

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router