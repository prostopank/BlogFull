<template>
  <div id="app">
    <registration/>
    <sign-in/>
    <all-article/>
  </div>
</template>

<script>

import AllArticle from './components/AllArticle.vue';
import Registration from './components/Registration.vue';
import SignIn from './components/SignIn.vue';
export default {
  name: "App",
  components:{
    AllArticle,
    Registration,
    SignIn
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
  margin: 60px auto;
  width: 400px;
}
</style>
