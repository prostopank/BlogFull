<template>
  <div class="ArticleAll">
    <div class="article">
      <h2>{{ article.title }}</h2>
      <p>{{ article.body }}</p>
      <p>{{ article.create_date }}</p>
    </div>
    <template v-if="authenticated">
      <button type="submit" @click="add_to_favorite()">Add to favorite</button><br><br>
      <form @submit.prevent="submit">
        <div>
          <label for="body"> Comment </label><br>
          <textarea
            type="text"
            name="body_comments"
            id="body_comments"
            cols="30" rows="5"
            v-model="body_comments"
          />
          
        </div>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
    </template>
    <template v-else> </template>
    <div
      class="article"
      v-for="comment in comments"
      :key="comment.id"
      v-bind:comments_data="comment"
    >
      <p>{{ comment.body }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "Article",
  data() {
    return {
      article: "",
      body_comments: "",
      comments: [],
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
      const comments = article.comments;
      this.comments = comments;
    }
  },

  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
      user: "auth/user",
    }),
  },

  methods: {
    async submit() {
      await axios
        .post("http://127.0.0.1:8000/api/comments/create", {
          user_id: this.user.id,
          article_id: this.article.id,
          body: this.body_comments,
        })
        .then((response) => {
          this.comments.push(response.data);
          this.body_comments = " ";
        });
    },
    async add_to_favorite(){
      await axios 
      .post("http://127.0.0.1:8000/api/favorite_articles/create", {
          user_id: this.user.id,
          article_id: this.article.id,
        })
    }
  },
};
</script>

<style>

</style>