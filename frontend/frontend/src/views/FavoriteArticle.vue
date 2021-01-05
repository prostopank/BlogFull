<template>
  <div class="ArticleAll">
    <h1>Favorite Articles</h1>

    <div
      class="article"
      v-for="article in favorite_articles"
      :key="article.id"
      v-bind:article_data="article"
    >
      <h2 class="header_style">{{ article.article_id.title }}</h2>

      <p>{{ article.article_id.body }}</p>
      <hr />
      <p>{{ article.article_id.create_date }}</p>
      <p>{{ article.article_id.views }}</p>
      <hr />
      <button
        class="button_style"
        style="background-color: red"
        type="submit"
        @click="delete_from_favorite(article.id)"
      >
        Delete
      </button>
      <button
        class="button_style"
        style="margin-left: 10px"
        @click="
          $router.push({
            name: 'ArticleDetail',
            params: { id: article.article_id.id },
          })
        "
      >
        Go to
      </button>
      <br /><br />
      <router-view />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
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

    async delete_from_favorite(article_id) {
      await axios
        .delete(
          "http://127.0.0.1:8000/api/favorite_articles/delete/" + article_id
        )
        .then(() => {
          const index = this.favorite_articles.findIndex(
            (article) => article.id === article_id
          );
          if (~index) this.favorite_articles.splice(index, 1);
        });
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
</style>