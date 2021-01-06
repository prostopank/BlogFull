<template>
  <div id="Registration">
    <form @submit.prevent="submit">
      <h1>Registration</h1>
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
        <button type="submit" class="button_style">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Registration",
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
      let responce = await axios.post("/auth/users/", this.form);
      console.log(responce.data);
    },
  },
};
</script>

<style>
#Registration {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 60px auto;
  width: 400px;
}
</style>
