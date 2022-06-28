<template>
  <v-row>
    <v-col cols="12" v-for="post in posts" :key="post.id">
      <PostCard :post="post" />
    </v-col>

    <v-card v-if="!posts.length">
      <v-card-title>Geen beroepsproducten gevonden</v-card-title>
      <v-card-text
        >Helaas zijn er geen beroepsproducten in uw portfolio gevonden, maak via
        de plus knop rechtsonderin een beroepsproduct aan.
      </v-card-text>
    </v-card>

    <v-btn
      color="primary"
      fab
      large
      fixed
      bottom
      right
      to="/beroepsproduct/inleveren"
    >
      <v-icon>mdi-plus</v-icon>
    </v-btn>
  </v-row>
</template>

<script lang="ts">
import { mapGetters } from 'vuex'
import Vue from 'vue'
import { GetPosts } from '~/types/GetPosts'

export default Vue.extend({
  name: 'IndexPage',
  data() {
    return {
      posts: [] as GetPosts,
    }
  },
  computed: {
    ...mapGetters('auth', ['userId']),
  },
  fetchOnServer: true,
  async fetch() {
    this.posts = await this.$axios.$get<GetPosts>(`/posts`)
  },
  middleware: ['authenticated'],
})
</script>
