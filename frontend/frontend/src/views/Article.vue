<template>
  <div class="ArticleAll">
    <div class="article">
      <h2>{{ article.title }}</h2>
      <p>{{ article.body }}</p>
      <p>{{ article.create_date }}</p>
      <p>{{ }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Article",
  data() {
    return {
      article: null,
    };
  },
  async created() {
    const res = await fetch("http://127.0.0.1:8000/api/article/all");
    const articles = await res.json();
    const article = articles.find(
      (article) => article.id == this.$route.params.id
    );
    axios.get("http://127.0.0.1:8000/api/article/{{article.id}}")
    if (article) {
      this.article = article;
    }
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