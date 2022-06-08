<template>
  <v-container fluid>
    <form method="post" @submit.prevent="submitForm">
      <div id="productTextContainer" class="container">
        <h1 class="textBoxTitle">
          Titel
        </h1>
        <v-hover />
        <v-text-field
          id="aspectTitel"
          v-model="values.title"
          class="textField"
          counter
          maxlength="255"
          type="text"
          placeholder="Schrijf hier je Titel van je aspect..."
          required
        />

        <div id="characterLimit">
          max. 255 characters
        </div>
      </div>

      <div id="productTextContainer" class="container">
        <h1 class="textBoxTitle">
          Korte Beschrijving
        </h1>
        <v-hover />
        <v-textarea
          id="aspectKorteBeschrijving"
          v-model="values.short_description"
          class="textField"
          counter
          maxlength="255"
          type="text"
          placeholder="Schrijf hier je korte beschrijving over dit aspect..."
          required
        />

        <div id="characterLimit">
          max. 255 characters
        </div>
      </div>

      <div id="productTextContainer" class="container">
        <h1 class="textBoxTitle">
          Beschrijving
        </h1>
        <v-hover />
        <v-textarea
          id="aspectBeschrijving"
          v-model="values.description"
          class="textField"
          counter
          maxlength="1000"
          type="text"
          placeholder="Schrijf hier je beschrijving over dit aspect..."
          required
        />

        <div id="characterLimit">
          max. 1000 characters
        </div>
      </div>

      <div id="productTextContainer" class="container">
        <h1 class="textBoxTitle">
          Link
        </h1>
        <v-hover />
        <v-text-field
          id="aspectLink"
          v-model="values.external_url"
          class="textField"
          counter
          maxlength="2000"
          type="text"
          placeholder="Schrijf hier je externe link van je aspect..."
          required
        />

        <div id="characterLimit">
          max. 2000 characters
        </div>
      </div>

      <div id="productTextContainer" class="container">
        <h1 class="textBoxTitle">
          Aspect Rating
        </h1>
        <v-hover />
        <v-select
          v-model="values.rating_ids"
          :items="cards"
          class="textField"
          hint="kies een rating"
          multiple
          item-text="title"
          item-value="id"
          chips
        />

        <div id="AspectRatingToevoegen">
          <v-btn
            class="Submit"
            @click="overlay = !overlay"
          >
            Aspect Rating Toevoegen
          </v-btn>
          <v-overlay :absolute="absolute" :value="overlay" class="overlay">
            <AspectRatingAanmaken />
            <v-btn width="100%" @click="overlay = false">
              Close
            </v-btn>
          </v-overlay>
        </div>
      </div>

      <v-btn
        type="submit"
        class="Submit"
      >
        Submit
      </v-btn>
    </form>
  </v-container>
</template>
<script>
import { axiosInstance } from '../../lib/axiosInstance'
import AspectRatingAanmaken from './AspectRatingAanmaken'

export default {
  name: 'AspectAanmaken',
  components: { AspectRatingAanmaken },
  data () {
    return {
      cards: [],
      values: {
        title: '',
        short_description: '',
        description: '',
        external_url: '',
        rating_ids: []
      },
      overlay: false,
      absolute: true
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
      axiosInstance.post('api/v1/aspects/', this.values)
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
#characterLimit{
  float: right;

}
</style>
