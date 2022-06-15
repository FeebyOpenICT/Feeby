<template>
  <v-app>
    <v-main class="grey lighten-2">
      <v-container>
        <v-col>
          <v-card>
            <v-card-title>
              {{ error.statusCode }} {{ error.title }}
            </v-card-title>
            <v-card-text v-if="error.message">
              {{ error.message }}
            </v-card-text>
            <v-card-subtitle>
              <NuxtLink to="/">Back Home</NuxtLink>
            </v-card-subtitle>
          </v-card>
        </v-col>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  props: {
    error: {
      type: Object,
      default: null,
    },
  },
  head() {
    return {
      title: this.error.title
    }
  },
}
</script>
