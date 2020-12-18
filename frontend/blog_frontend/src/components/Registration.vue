<template>
  <div id="Registration">
    <form @submit.prevent="submit">
      {{ form }}
      <div>
        <label for="Username"> Username </label>

        <input
          type="text"
          name="username"
          id="username"
          v-model="form.username"
        />
      </div>
      <div>
        <label for="password"> Password </label>

        <input
          type="password"
          name="password"
          id="password"
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
      let responce = await axios.post("auth/users/", this.form);
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
