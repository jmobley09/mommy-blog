<template>
  <v-container grid-list-xl>
    <v-layout wrap>
      <v-flex xs12>
        <slot />
      </v-flex>
      <v-divider />
      <feed-card
        v-for="(article) in parenting"
        :key="article.title"
        :size="3"
        :value="article"
      />
      <v-divider />
      <feed-card
        v-for="(article) in essential_oils"
        :key="article.title"
        :size="3"
        :value="article"
      />
    </v-layout>
  </v-container>
</template>

<script>
// Utilities
  import { mapState } from 'vuex'

  export default {
    name: 'Feed',

    components: {
      FeedCard: () => import('@/components/FeedCard')
    },

    data: () => ({}),

    computed: {
      ...mapState(['articles']),
      parenting () {
        let categorized = this.articles.filter(
          article => article.category === 'Parenting'
        )
        console.log(categorized)
        return categorized
      },
      essential_oils () {
        let categorized = this.articles.filter(
          article => article.category === 'Essential Oils'
        )
        console.log(categorized)
        return categorized
      }
    }
  }
</script>
