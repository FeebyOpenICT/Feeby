<template>
  <form @submit.prevent="submitForm">
    <div id="productTextContainer" class="container">
      <h1 class="textBoxTitle">
        Titel
      </h1>
      <v-hover />
      <v-textarea
        id="aspectTitel"
        v-model="values.title"
        class="textField"
        counter
        :max-length="255"
        type="text"
        placeholder="Schrijf hier je Titel van je aspect..."
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
        :max-length="1000"
        type="text"
        placeholder="Schrijf hier je beschrijving over dit aspect..."
      />

      <div id="characterLimit">
        max. 1000 characters
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
        :max-length="255"
        type="text"
        placeholder="Schrijf hier je korte beschrijving over dit aspect..."
      />

      <div id="characterLimit">
        max. 255 characters
      </div>
    </div>
    <div id="productTextContainer" class="container">
      <h1 class="textBoxTitle">
        Link
      </h1>
      <v-hover />
      <v-textarea
        id="aspectLink"
        v-model="values.external_url"
        class="textField"
        counter
        :max-length="2000"
        type="text"
        placeholder="Schrijf hier je externe link van je aspect..."
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
      <v-list class="aspectRatingsBox">
        <v-list-item-group>
          <v-list-item
            v-for="rating in cards"
            :key="rating.id"
          >
            <v-list-item-content>
              <v-list-item-title v-text="rating.title" />
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>

      <v-btn
        @click="overlay = !overlay"
      >
        Aspect Rating Toevoegen
      </v-btn>
      <v-overlay :value="overlay" class="overlay">
        <v-overlay-content>
          <AspectRatingAanmaken />
        </v-overlay-content>
        <br>
        <v-btn width="100%" @click="overlay = false">
          Close
        </v-btn>
      </v-overlay>
    </div>
  </form>
</template>
<script>
import { axiosInstance } from '../../lib/axiosInstance'
import AspectRatingAanmaken from './AspectRatingAanmaken'
export default {
  name: 'AspectAanmaken',
  components: { AspectRatingAanmaken },
  data () {
    return {
      cards: null,
      values: {
        title: '',
        short_description: '',
        description: '',
        external_url: '',
        rating_ids: ''
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
        }).finally(() => {
          // Perform action in always
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
