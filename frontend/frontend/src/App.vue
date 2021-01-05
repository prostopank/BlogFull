<template>
  <div id="app">
    <template v-if="authenticated">
      
      <div style="text-align: right; margin-right: 5%">
        <span>{{ user.username }}</span>
        <br>
      <router-link to="/">Home </router-link>
      <router-link to="/FavoriteArticle">Favorite Articles </router-link>
      <router-link to="/Edit">Edit </router-link>
      <a href="#" @click.prevent="signOut">SignOut</a>
      </div>
    </template>
    <template v-else>
      <div style="text-align: right; margin-right: 5%">
      <router-link to="/">Home </router-link>
      <router-link to="/SignIn">SignIn </router-link>
      <router-link to="/Registration">Registration </router-link>
      </div>
    </template>

    <br />
    <hr>
    <router-view />
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
  methods: {
    ...mapActions({
      signOutAction: "auth/signOut",
    }),

    signOut() {
      try {
        this.signOutAction()
          .then(() => {
            this.$router.replace({
              name: "Home",
            });
          })
          .catch(() => {
            console.log("failed");
          });
      } catch (error) {
        console.log("Error");
      }
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  color: #2c3e50;
  margin-top: 60px;
  text-align: center;
  
}
</style>
