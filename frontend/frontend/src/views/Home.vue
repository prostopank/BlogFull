<template>
  <div class="ArticleAll">
    <h1>Articles</h1>
    <div
      class="article"
      v-for="article in articles"
      :key="article.id"
      v-bind:article_data="article"
    >
      <h2 class="header_style">{{ article.title }}</h2>

      <p>{{ article.body }}</p>
      <hr />
      <span>Create date: {{ article.create_date }} </span>
      <span>Views: {{ article.views }}</span>
      <hr />
      <button
        class="button_style"
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
  margin-top: 40px;
  text-align: center;
}
.article {
  border: 2px solid rgb(0, 0, 0);
  border-radius: 20px;
  margin-bottom: 2rem;
  width: 600px;
  margin-left: 34%;
  background-color: white;
}

.button_style {
  border-radius: 10px;
  width: 150px;
  height: 40px;
  font-size: 18px;
  font-weight: bold;
  color: rgb(18, 0, 82);
  background-color: rgba(26, 80, 228, 0.336);
}

.header_style {
  margin-block-start: 0;
  margin-block-end: 0;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  background-color: rgba(26, 80, 228, 0.336);
  padding-block-end: 10px;
  padding-block-start: 10px;
}
</style>