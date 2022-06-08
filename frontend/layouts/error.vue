<template>
  <v-app>
    <v-main class="grey lighten-2">
      <v-container fluid>
        <v-card>
          <v-card-title v-if="error.statusCode === 404">
            {{ pageNotFound }}
          </v-card-title>
          <v-card-title v-else>
            {{ otherError }}
          </v-card-title>
          <v-card-subtitle>
            <NuxtLink to="/">Back Home</NuxtLink>
          </v-card-subtitle>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'EmptyLayout',
  layout: 'empty',
  props: {
    error: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
      pageNotFound: '404 Not Found',
      otherError: 'An error occurred',
    }
  },
  head() {
    const title =
      this.error.statusCode === 404 ? this.pageNotFound : this.otherError
    return {
      title,
    }
  },
}
</script>

<style scoped>
h1 {
  font-size: 20px;
}
</style>
