<template>
  <v-container fluid>
    <v-card class="RatingUpdateCard">
      <h1 class="AspectRatingTitle">
        Aspect Rating Aanpassen
      </h1>
      <form @submit.prevent="submitForm">
        <div id="productTextContainer" class="container">
          <h2 class="textBoxTitle">
            Titel
          </h2>
          <v-divider />
          <h3 class="textBoxOldTitle">
            Oude Versie
          </h3>
          <p v-for="card in cards" :key="card.id">
            test
            {{ card.title }}
          </p>
          <v-divider />
          <v-text-field
            id="AspectRatingTitel"
            v-model="ratings.title"
            class="textField"
            counter
            maxlength="255"
            type="text"
            placeholder="Vul De Nieuwe Titel Hierin..."
          />

          <div id="characterLimit">
            max. 255 characters
          </div>
        </div>
        <v-divider />
        <div id="productTextContainer" class="container">
          <h2 class="textBoxTitle">
            Korte Beschrijving
          </h2>
          <v-divider />
          <h3 class="textBoxOldTitle">
            Oude Versie
          </h3>
          <p v-for="card in cards" :key="card.id">
            {{ card.short_description }}
          </p>
          <v-divider />
          <v-textarea
            id="AspectRatingKorteBeschrijving"
            v-model="ratings.short_description"
            class="textField"
            counter
            maxlength="255"
            type="text"
            placeholder="Vul De Nieuwe Korte Beschrijving Hierin..."
          />

          <div id="characterLimit">
            max. 255 characters
          </div>
        </div>
        <v-divider />
        <div id="productTextContainer" class="container">
          <h2 class="textBoxTitle">
            Beschrijving
          </h2>
          <v-divider />
          <h3 class="textBoxOldTitle">
            Oude Versie
          </h3>
          <p v-for="card in cards" :key="card.id">
            {{ card.description }}
          </p>
          <v-divider />
          <v-textarea
            id="AspectRatingBeschrijving"
            v-model="ratings.description"
            class="textField"
            counter
            maxlength="1000"
            type="text"
            placeholder="Vul De Nieuwe Beschrijving Hierin..."
          />

          <div id="characterLimit">
            max. 1000 characters
          </div>
        </div>
        <v-btn
          id="submitButton"
          type="submit"
          class="Submit"
        >
          Opslaan
        </v-btn>
      </form>
    </v-card>
  </v-container>
</template>

<script>
import { axiosInstance } from '../../lib/axiosInstance'
export default {
  name: 'AspectRatingAanmaken',
  data () {
    return {
      cards: null,
      ratings: {
        title: '',
        short_description: '',
        description: ''
      }
    }
  },
  mounted () {
    axiosInstance
      .get('api/v1/ratings/')
      .then(response => (this.cards = response.data))
      .catch(error => console.log(error))
      .then(console.log(this.cards))
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
        })
    },
    updateForm () {
      axiosInstance.patch('api/v1/ratings/', this.ratings)
        .then((response) => {
          // Perform Success Action
          console.log(response)
        })
        .catch((error) => {
          // error.response.status Check status code
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
@import '.css/styles.css';
.AspectRatingTitle {
  position: relative;
  margin: 2% 40%;
}
</style>
