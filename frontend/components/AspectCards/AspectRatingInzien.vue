<template>
  <v-container fluid>
    <v-card
      class="mx-auto"
      max-width="400"
      max-height="500"
      tile
      outlined
      elevation="2"
      margin="15"
    >
      <h1
        class="AspectRatingH1"
        align="center"
      >
        Aspect Rating Lijst
      </h1>
      <v-list class="overflow-auto" max-height="500">
        <v-list-item-group color="#0079CF">
          <v-list-item
            v-for="rating in ratings"
            :key="rating.id"
            two-line
          >
            <v-list-item-content>
              <v-list-item-title v-text="rating.title" />
              <v-list-item-subtitle v-text="rating.short_description" />
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon>{{ icons.mdiPencil }}</v-icon>
            </v-list-item-icon>
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

.AspectRatingH1 {
  font-size: 20px;
  background-color: #0079CF;
  color: white;
  margin-bottom: 0;
  padding: 15px;
}

</style>
