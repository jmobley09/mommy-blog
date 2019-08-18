<template>
  <v-container grid-list-xl>
    <v-layout wrap>
      <v-flex xs12>
        <slot />
      </v-flex>

      <feed-card v-for="(article) in homeArticles" :key="article.title" :size="3" :value="article" />
    </v-layout>
  </v-container>
</template>

<script>
// Utilities
import { mapState } from "vuex";
require(["underscore"]);

export default {
  name: "Feed",

  components: {
    FeedCard: () => import("@/components/FeedCard")
  },

  data: () => ({}),

  computed: {
    ...mapState(["articles"]),
    homeArticles() {
      const categorized = _.groupBy(this.articles, "category");

      // let categorized = this.articles.filter(
      //   article => article.category == "Parenting"
      // );
      console.log(categorized);
      return categorized;
    }
  },

  watch: {
    page() {
      window.scrollTo(0, 0);
    }
  }
};
</script>
