import Vue from 'vue'
import VueRouter from 'vue-router'

import SignIn from '../views/SignIn.vue'
import Registration from '../views/Registration.vue'
import Home from '../views/Home.vue'
import Article from '../views/Article.vue'
import FavoriteArticle from '../views/FavoriteArticle.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/article/:id',
        name: 'ArticleDetail',
        component: Article
    },
    {
        path: '/SignIn',
        component: SignIn
    },
    {
        path: '/Registration',
        component: Registration
    },
    {
        path: '/FavoriteArticle',
        component: FavoriteArticle
    }

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router