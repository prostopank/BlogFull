<template>
  <div id="SignIn">
    <form @submit.prevent="submit">
      {{ form }}
      <div>
        <label for="Username"> Username </label>

        <input
          type="text"
          name="username"
          id="username_for_signin"
          v-model="form.username"
        />
      </div>
      <div>
        <label for="password1"> Password </label>

        <input
          type="password"
          name="password"
          id="password_for_signin"
          v-model="form.password"
        />
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
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
    async submit() {
      let responce = await axios.post("auth/token", this.form);
      console.log(responce.data.token);
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
  margin: 60px auto;
  width: 400px;
}
</style>
