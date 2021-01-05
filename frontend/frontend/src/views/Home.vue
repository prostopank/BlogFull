<template>
  <div class="ArticleAll">
    <h1>Articles</h1>
    <div
      class="article"
      v-for="article in articles"
      :key="article.id"
      v-bind:article_data="article"
    >
      <h2>{{ article.title }}</h2>
      <hr />
      <p>{{ article.body }}</p>
      <hr />
      <p>{{ article.create_date }}</p>
      <p>Views: {{ article.views }}</p>
      <hr />
      <button
        @click="
          $router.push({ name: 'ArticleDetail', params: { id: article.id } })
        "
      >
        Go to</button
      ><br />
      <br />
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "AllArticle",
  data() {
    return {
      articles: [],
    };
  },
  async mounted() {
    const res = await fetch("http://127.0.0.1:8000/api/article/all");
    const articles = await res.json();
    this.articles = articles;
  },
};
</script>

<style>
.ArticleAll {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 60px;
  text-align: center;
}
.article {
  border: 2px solid #ccc;
  border-radius: 20px;
  margin-bottom: 2rem;
  width: 600px;
  margin-left: 34%;
}
</style>