<template>
  <div class="ArticleAll">
    <div
      class="article"
      v-for="article in user_articles"
      :key="article.id"
      v-bind:article_data="article"
    >
      <h2>{{ article.title }}</h2>
      <p>{{ article.body }}</p>
      <p>{{ article.create_date }}</p>
      <p>{{ article.views }}</p>

      <button
        @click="
          $router.push({ name: 'ArticleDetail', params: { id: article.id } })
        "
      >
        Go to
      </button>
      <button type="edit">Edit</button>
      <button @click="delete_article(article.id)">Delete</button>
      <p>{{ article.id }}</p>
      <router-view />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
export default {
  name: "Edit",
  data() {
    return {
      articles: [],
      user_articles: [],
      Title: "",
      Body: "",
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
      let user_articles = await [];
      for (let i = 0; i < Object.keys(this.articles).length; i++) {
        if (this.articles[i].user_id.username == this.user.username) {
          user_articles.push(this.articles[i]);
        }
      }
      this.user_articles = user_articles;
    },
    async delete_article(article_id) {
      await axios
        .delete("http://127.0.0.1:8000/api/article/delete/" + article_id)
        .then(() => {
          const index = this.user_articles.findIndex(
            (article) => article.id === article_id
          );
          if (~index) this.user_articles.splice(index, 1);
        });
    },
  },
  async mounted() {
    const res = await fetch("http://127.0.0.1:8000/api/article/all");
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
  width: 450px;
}
.article {
  border: 1px solid #ccc;
  border-radius: 20px;
  margin-bottom: 2rem;
  width: 400px;
}
</style>