<template>
  <div id="app">
    <template v-if="authenticated">
      <p>{{user.username}}</p>
      <router-link to="/">Home </router-link> 
      <a href="#" @click.prevent="signOut">SignOut</a>
    </template>
    <template v-else>
      <router-link to="/">Home </router-link>
      <router-link to="/SignIn">SignIn </router-link> 
      <router-link to="/Registration">Registration </router-link>
    </template>
    
    <br>
    <router-view/>
  </div>
</template>

<script>

import { mapGetters, mapActions } from "vuex";

export default {
 

  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
      user: "auth/user",
    }),
  },
  methods:{
    ...mapActions({
      signOutAction:'auth/signOut'
    }),

    signOut(){
      try {
        this.signOutAction().then(()=>{
        this.$router.replace({
          name:'Home'
        })
      }).catch(()=>{
        console.log('failed')
      })
      } catch (error) {
        console.log('Error')
      }
  }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
