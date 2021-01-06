<template>
  <div class="SignIn">
    <form @submit.prevent="submit">
      <br /><br /><br>
       <h1>Authorization</h1>
      <div>
        <input
          type="text"
          name="username"
          id="username"
          v-model="form.username"
          class="form_style"
          placeholder="Username"
        />
      </div>
      <div>
        <input
          type="password"
          name="password"
          id="password"
          v-model="form.password"
          class="form_style"
          placeholder="Password"
        />
      </div>
      <div>
        <button type="submit" class="button_style">Sign in</button>
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
      this.signIn(this.form)
        .then(() => {
          this.$router.replace({
            name: "Home",
          });
        })
        .catch(() => {
          console.log("failed");
        });
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

.form_style {
  border-radius: 20px;
  width: 300px;
  height: 35px;
  margin-bottom: 10px;
  text-align: center;
  font-size: 18px;
}
</style>