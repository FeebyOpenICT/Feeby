<template>
  <v-card class="RatingCard">
    <form @submit.prevent="submitForm">
      <div id="productTextContainer" class="container">
        <h2 class="textBoxTitle">
          Titel
        </h2>
        <v-hover />
        <v-textarea
          id="AspectRatingTitel"
          v-model="ratings.title"
          class="textField"
          counter
          :max-length="255"
          type="text"
          placeholder="Schrijf hier je titel van je aspect rating..."
        />

        <div id="characterLimit">
          max. 255 characters
        </div>
      </div>
      <div id="productTextContainer" class="container">
        <h2 class="textBoxTitle">
          Beschrijving
        </h2>
        <v-hover />
        <v-textarea
          id="AspectRatingBeschrijving"
          v-model="ratings.description"
          class="textField"
          counter
          :max-length="1000"
          type="text"
          placeholder="Schrijf hier je beschrijving over dit aspect rating..."
        />

        <div id="characterLimit">
          max. 1000 characters
        </div>
      </div>
      <div id="productTextContainer" class="container">
        <h2 class="textBoxTitle">
          Korte Beschrijving
        </h2>
        <v-hover />
        <v-textarea
          id="AspectRatingKorteBeschrijving"
          v-model="ratings.short_description"
          class="textField"
          counter
          :max-length="255"
          type="text"
          placeholder="Schrijf hier je korte beschrijving over dit aspect rating..."
        />

        <div id="characterLimit">
          max. 255 characters
        </div>
      </div>
      <v-btn
        type="submit"
        width="90%"
      >
        Opslaan
      </v-btn>
    </form>
  </v-card>
</template>
<script>
import { axiosInstance } from '../../lib/axiosInstance'
export default {
  name: 'AspectRatingAanmaken',
  data () {
    return {
      ratings: {
        title: '',
        short_description: '',
        description: ''
      }
    }
  },
  methods: {
    submitForm () {
      axiosInstance.post('api/v1/ratings/', this.ratings)
        .then((response) => {
          // Perform Success Action
          console.log(response)
        })
        .catch((error) => {
          // error.response.status Check status code
          console.log(error)
        }).finally(() => {
          // Perform action in always
        })
    }
  }
}
</script>
<style scoped>
@import '.css/styles.css';
</style>
