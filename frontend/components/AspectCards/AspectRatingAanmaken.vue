<template>
  <v-card>
    <form onsubmit="handleSubmit">
      <div id="productTextContainer" class="container">
        <h1 class="textBoxTitle">
          Titel
        </h1>
        <v-hover />
        <v-textarea
          id="AspectRatingTitel"
          class="textField"
          :max-length="255"
          :value="values.title"
          type="text"
          placeholder="Schrijf hier je titel van je aspect rating..."
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
          id="AspectRatingBeschrijving"
          class="textField"
          counter
          :max-length="1000"
          :value="values.description"
          type="text"
          placeholder="Schrijf hier je beschrijving over dit aspect rating..."
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
          id="AspectRatingKorteBeschrijving"
          class="textField"
          counter
          :max-length="255"
          :value="values.short_description"
          type="text"
          placeholder="Schrijf hier je korte beschrijving over dit aspect rating..."
        />

        <div id="characterLimit">
          max. 255 characters
        </div>
      </div>
      <v-btn type="submit">
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
      values: {
        title: '',
        short_description: '',
        description: ''
      },
      overlay: false
    }
  },
  mounted () {
    axiosInstance
      .post('api/v1/ratings/', this.methods.userData)
      .then((response) => {
        // eslint-disable-next-line no-console
        console.log(response)
      })
  },
  methods: {
    handleSubmit: (e) => {
      e.preventDefault()
    },
    userData: {
      title: this.values.title,
      short_description: this.values.short_description,
      description: this.values.description
    }
  }
}
</script>
<style scoped>
@import '.css/styles.css';
</style>
