<template>
  <div class="ArticleAll">
    <div class="article">
      <h2>{{ article.title }}</h2>
      <p>{{ article.body }}</p>
      <p>{{ article.create_date }}</p>
    </div>
    <form @submit.prevent="submit">
    <div>
      <label for="body"> Comment </label>
      <textarea type="text" name="body_comments" id="body_comments" v-model="body_comments" />
    </div>
    <div>
      <button type="submit">Submit</button>
    </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Article",
  data() {
    return {
      article: "",
      body_comments: "",
    };
  },
  async created() {
    const res = await fetch("http://127.0.0.1:8000/api/article/all");
    const articles = await res.json();
    const article = articles.find(
      (article) => article.id == this.$route.params.id
    );
    //axios.get("http://127.0.0.1:8000/api/article/{{article.id}}");
    if (article) {
      this.article = article;
    }
  },

  methods: {
    async submit() {
      
      await axios.post("http://127.0.0.1:8000/api/comments/create", {
        article_id: this.article.id,
        body: this.body_comments,
      });
    },
  },
};
</script>

<style>
.ArticleAll {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 60px auto;
  width: 400px;
}
.article {
  border: 1px solid #ccc;
  border-radius: 20px;
  margin-bottom: 2rem;
  width: 400px;
}
</style>