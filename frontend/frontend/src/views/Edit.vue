<template>
  <div class="ArticleAll">
    <button class="button" @click="show_edit_page = true">Add Article</button
    ><br />
    <template v-if="show_edit_page">
      <form @submit.prevent="create_article">
        <div>
          <br />
          Title<br />
          <input
            type="text"
            name="article.title"
            v-model="article_title_edit"
          /><br /><br />
          Body<br />
          <textarea
            name="article.body"
            v-model="article_body_edit"
            cols="30"
            rows="10"
          ></textarea
          ><br />
          <button class="button" @click="close_form()">Close</button>
          <button class="button" style="margin-left: 10px">Save</button>
        </div>
      </form> </template
    ><br />

    <div
      class="article"
      v-for="article in user_articles"
      :key="article.id"
      v-bind:article_data="article"
    >
      <h2>{{ article.title }}</h2><hr>
      <p>{{ article.body }}</p><hr>
      <p>{{ article.create_date }}</p>
      <p>{{ article.views }}</p><hr>

      <button
        @click="
          $router.push({ name: 'ArticleDetail', params: { id: article.id } })
        "
      >
        Go to</button
      ><br />
      <br />
      <button class="button" @click="edit_article(article)">
        Edit Article
      </button>

      <button @click="delete_article(article.id)" style="margin-left: 10px">
        Delete
      </button>
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
      show_edit_page: false,

      article_title_edit: "",
      article_body_edit: "",
      article_id: "",
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

    async create_article() {
      await axios
        .post("http://127.0.0.1:8000/api/article/create", {
          user_id: this.user.id,
          title: this.article_title_edit,
          body: this.article_body_edit,
        })
        .then((response) => {
          this.user_articles.push(response.data);
          this.close_form();
        });
    },

    async edit_article(article) {
      this.show_edit_page = true;
      this.article_title_edit = article.title;
      this.article_body_edit = article.body;
      this.article_id = article.id;
    },

    async close_form() {
      this.show_edit_page = false;
      this.article_title_edit = "";
      this.article_body_edit = "";
      this.article_id = "";
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
</style>