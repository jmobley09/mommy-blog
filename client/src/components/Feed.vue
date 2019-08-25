<template>
  <v-container
    grid-list-xl
  >
    <v-layout wrap>
      <v-flex xs12>
        <slot />
      </v-flex>

      <feed-card
        v-for="(article) in homeArticles"
        :key="article.title"
        :size="3"
        :value="article"
      />
    </v-layout>
  </v-container>
</template>

<script>
  // Utilities
  import {
    mapState
  } from 'vuex'

  export default {
    name: 'Feed',

    components: {
      FeedCard: () => import('@/components/FeedCard')
    },

    data: () => ({
    }),

    computed: {
      ...mapState(['articles']),
      homeArticles () {
        // sets mapped articles to local variable to get rid of "this" keyword
        // makes filter function malfunction if this keyword is included
        const articles = this.articles; 

        // filters the articles to match the one passed in
        let filtered = articles.filter(article => article.category === "Essential Oils");

        // used to hold first 3 articles
        const firstThree = [];

        // determines first 3 articles in list
        for(let i = 0; i < 3; i++) {
          firstThree.push(filtered[i]);
        }

        return firstThree;
      }
    }
  }
</script>
