<template>
  <div>
    <template v-if="posts.length">
      <v-col v-for="post in posts" :key="post.id">
        <PostCard :post="post"/>
      </v-col>
    </template>
    <v-card v-else>
      <v-card-title>Geen beroepsproducten gevonden</v-card-title>
      <v-card-text
      >Helaas zijn er geen beroepsproducten in uw portfolio gevonden, maak via
        de plus knop rechtsonderin een beroepsproduct aan.
      </v-card-text
      >
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
  </div>
</template>

<script lang="ts">
import {mapGetters} from 'vuex'
import Vue from "vue";
import {GetPosts} from "~/types/GetPosts";

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
    this.posts = await this.$axios.$get<GetPosts>(`/users/${this.userId}/posts`)
  },
  middleware: ['authenticated'],
})
</script>
