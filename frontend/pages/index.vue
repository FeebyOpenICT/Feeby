<template>
  <div>
    <beroepsproduct
      title="Test Beroepsproduct"
      description="Dit is een test beschrijving"
    />

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
import Beroepsproduct from '~/components/Beroepsproduct.vue'
import { mapGetters } from 'vuex'
export default {
  components: { Beroepsproduct },
  name: 'IndexPage',
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
