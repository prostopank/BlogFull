<template>
  <div id="SignIn">
    <form @submit.prevent="submit">
      <div>
        <label for="username"> username </label>
        <input
          type="text"
          name="username"
          id="username"
          v-model="form.username"
        />
      </div>
      <div>
        <label for="password"> password </label>
        <input
          type="password"
          name="password"
          id="password"
          v-model="form.password"
        />
      </div>
      <div>
        <button type="submit">Sign in</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "SignIn",
  components: {},

  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    ...mapActions({
      signIn: "auth/signIn",
    }),

    submit() {
      this.signIn(this.form);
    },
    
  },
};
</script>

<style>
#SignIn {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>