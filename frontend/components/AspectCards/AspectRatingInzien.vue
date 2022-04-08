<template>
  <v-container fluid>
    <v-card
      class="mx-auto"
      max-width="400"
      tile
    >
      <v-list>
        <v-list-item-group
          multiple
          color="#0079CF"
        >
          <v-list-item
            v-for="rating in ratings"
            :key="rating.id"
            two-line
          >
            <v-list-item-content>
              <v-list-item-title v-text="rating.title" />
              <v-list-item-subtitle v-text="rating.short_description" />
              <v-list-item-icon>
                <v-icon>{{ icons.mdiPencil }}</v-icon>
              </v-list-item-icon>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card>
  </v-container>
</template>

<script>
import { mdiPencil } from '@mdi/js'
import { axiosInstance } from '~/lib/axiosInstance'
export default {
  name: 'AspectRatingInzien',
  data () {
    return {
      ratings: null,
      icons: {
        mdiPencil
      }
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
@import '.css/styles.css';

</style>
