<template>
  <v-container grid-list-xl>
    <v-layout wrap>
      <v-flex xs12>
        <slot />
      </v-flex>
      <div class="divider" >Parenting
        <v-divider></v-divider>
      </div>

      <feed-card
        v-for="(article) in parenting"
        :key="article.title"
        :size="3"
        :value="article"
      />
      <div class="divider" >Essential Oils
        <v-divider></v-divider>
      </div>
      <feed-card
        v-for="(article) in essential_oils"
        :key="article.title"
        :size="3"
        :value="article"
      />
      <div class="divider" >Recipes
        <v-divider></v-divider>
      </div>
      <feed-card
        v-for="(article) in recipes"
        :key="article.title"
        :size="3"
        :value="article"
      />
      <div class="divider" >Wellness
        <v-divider></v-divider>
      </div>
      <feed-card
        v-for="(article) in wellness"
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

        return this.firstThree(categorized);
      },
      essential_oils () {
        let categorized = this.articles.filter(
          article => article.category === 'Essential Oils'
        )
        return this.firstThree(categorized);
      },
      recipes () {
        let categorized = this.articles.filter(
          article => article.category === 'Recipes'
        )
        return this.firstThree(categorized);
      },
      wellness () {
        let categorized = this.articles.filter(
          article => article.category === 'Wellness'
        )
        return this.firstThree(categorized);
      }
    },

    methods: {
      firstThree(arr) {
        let first_three = [];

        for (let i =0; i < 3; i++) {
          first_three.push(arr[i]);
        }

        return first_three;
      }
    }
  }
</script>

<style scoped>
.divider {
  width: 100%;
  text-align: center;
  font-size: 300%;
}
</style>
