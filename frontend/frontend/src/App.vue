<template>
  <div id="app">
    <div class="nav">
      <template v-if="authenticated">
        <div style="text-align: right; margin-right: 5%">
          <br />

          <br />
          <span
            class="nav_link"
            style="background-color: rgba(255, 20, 0, 0.53);"
            >{{ user.username }}</span
          >
          <router-link to="/" class="nav_link">Home </router-link>
          <router-link to="/FavoriteArticle" class="nav_link"
            >Favorite Articles
          </router-link>
          <router-link to="/Edit" class="nav_link">Edit </router-link>
          <a href="#" @click.prevent="signOut" class="nav_link" style="background-color:rgba(255, 50, 0, 0.84)">SignOut</a>
        </div>
      </template>
      <template v-else>
        <br />
        <br />
        <div style="text-align: right; margin-right: 5%">
          <router-link to="/" class="nav_link">Home </router-link>
          <router-link to="/SignIn" class="nav_link">SignIn </router-link>
          <router-link to="/Registration" class="nav_link"
            >Registration
          </router-link>
        </div>
      </template>
      <br />
      <router-view />
    </div>
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
  text-align: center;
  padding: 0;
  margin: 0;
  
}

.nav {
  background: rgba(0, 0, 0, 0.63);
  width: 100%;
  height: 90px;
  position: absolute;
  left: 0;
  border: 1px solid rgb(0, 0, 0);
}

.nav_link {
  border: 0px solid rgb(0, 0, 0);
  border-radius: 5px;
  background-color: rgba(0, 0, 0, 0.562);
  font-size: 18px;
  margin-right: 10px;
  margin-left: 5px;
  text-decoration: none;
  padding-right: 15px;
  padding-left: 18px;
  padding-top: 10px;
  padding-bottom: 10px;
  color: rgb(255, 255, 255);
}
</style>
