<template>
  <v-container fluid>
    <v-list
      v-for="rating in ratings"
      :key="rating.id"
    >
      <v-list-title>
        {{ rating.title }}
      </v-list-title>
      <v-list-content>
        <v-list-text>
          {{ rating.short_description }}
          <br>
          {{ rating.description }}
        </v-list-text>
      </v-list-content>
    </v-list>
  </v-container>
</template>

<script>
import { axiosInstance } from '~/lib/axiosInstance'
export default {
  name: 'AspectRatingInzien',
  data () {
    return {
      ratings: null
    }
  },
  mounted () {
    axiosInstance
      .get('api/v1/ratings/')
      .then(response => (this.ratings = response.data))
      .catch(error => console.log(error))
  }
}
</script>

<style scoped>

</style>
