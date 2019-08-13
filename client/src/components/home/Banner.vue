<template>
  <base-card dark>
      <!-- <v-img
          v-for="image in images"
          :key="image"
          class="grey lighten-2"
          height="400"
          width="100%"
          :src="require('@/assets/instagram/' + image)"
        > -->
      <!-- <v-layout
        fill-height
        align-center
        pa-3
      >
        <v-flex
          xs12
          md7
          offset-md5
        >
          <h1 class="display-3 font-weight-light">
            The Art Of Travel
          </h1>
          <div class="subheading text-uppercase pl-2 mb-4">
            Finding Beauty, One flight at a time
          </div>
          <v-btn
            color="primary"
            depressed
            round
          >
            Subscribe
          </v-btn>
        </v-flex>
      </v-layout>-->

      <v-carousel>
        <v-carousel-item
          v-for="(image, i) in images"
          :key="i"
          class="grey lighten-2"
          height="400"
          width="100%"
          :src="image"
        >
         <v-row class="fill-height" align="center" justify="center">
            <div class="display-3">{{titles[i]}}</div>
          </v-row>
        </v-carousel-item>
      </v-carousel>
  </base-card>
</template>

<script>
  export default {
    data () {
      return {
        colors: [
          'primary',
          'secondary',
          'yellow darken-2',
          'red',
          'orange',
        ],
        titles: [
          'About',
          'Essential Oils',
          'Parenting',
          'Recipes',
          'Wellness',
        ],
        images: [
          'https://waywintechnologies.com/images/abouts/about-us-1024x683.jpg',
          'https://i1.wp.com/carepluslivingsolutions.com.au/wp-content/uploads/2015/05/gardenmortarpestle-slider4.jpg?fit=1137%2C500&ssl=1',
          'https://riseandshine.childrensnational.org/wp-content/uploads/2017/09/Development-boy-with-measuring-tape-1137x500.jpg',
          'https://www.gazettenet.com/getattachment/10be4549-3214-4aad-b09b-02d96e21c1f7/c1-18Food-Tasting-menu-from-Norway-021817-ph15',
          'http://www.gygicookingclasses.com/wp-content/uploads/2015/03/Cooking-Class-Main-Image-1.jpg',
        ]
      }
    },
  }
</script>