<template>
  <div>
    <template v-if="posts.length">
      <v-col v-for="post in posts">
        <BeroepsProduct
          :title="post.title"
          :description="post.description"
          :key="post.id"
        />
      </v-col>
    </template>
    <v-card v-else>
      <v-card-title>Geen beroepsproducten gevonden</v-card-title>
      <v-card-text
        >Helaas zijn er geen beroepsproducten in uw portfolio gevonden, maak via
        de plus knop rechtsonderin een beroepsproduct aan.</v-card-text
      >
    </v-card>

    <v-btn
      color="primary"
      fab
      large
      fixed
      bottom
      right
      to="/beroepsproduct-inleveren"
    >
      <v-icon>mdi-plus</v-icon>
    </v-btn>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'IndexPage',
  data() {
    return {
      posts: [],
    }
  },
  computed: {
    ...mapGetters('auth', ['userId']),
  },
  fetchOnServer: true,
  async fetch() {
    this.posts = await this.$axios.$get(`/users/${this.userId}/posts`)
  },
  middleware: ['authenticated'],
}
</script>
