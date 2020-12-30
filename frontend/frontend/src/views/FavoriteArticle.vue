<template>
  <div class="ArticleAll">
    <h1>Articles</h1>

    <div
      class="article"
      v-for="article in favorite_articles"
      :key="article.id"
      v-bind:article_data="article"
    >
      <h2>{{ article.article_id.title }}</h2>
      <p>{{ article.article_id.body }}</p>
      <p>{{ article.article_id.create_date }}</p>
      <p>{{ article.article_id.views }}</p>

      <button
        @click="
          $router.push({ name: 'ArticleDetail', params: { id: article.id } })
        "
      >
        Go to
      </button>
      <p>{{ article.id }}</p>
      <router-view />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "FavoriteArticle",
  data() {
    return {
      articles: [],
      favorite_articles: [],
    };
  },

  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
      user: "auth/user",
    }),
  },
  methods: {
    async filter_articles() {
      let favorite_articles = await [];
      for (let i = 0; i < Object.keys(this.articles).length; i++) {
        if (this.articles[i]["user_id"] == this.user.id) {
          favorite_articles.push(this.articles[i]);
        }
      }
      this.favorite_articles = favorite_articles;
    },
  },
  async mounted() {
    const res = await fetch("http://127.0.0.1:8000/api/favorite_articles/all");
    let articles = await res.json();
    this.articles = articles;
    this.filter_articles();
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