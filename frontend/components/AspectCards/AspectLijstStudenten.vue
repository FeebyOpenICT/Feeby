<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <!-- Data Tabel -->
  <v-data-table
    :value="selectedAspects"
    @input="$emit('update:selectedAspects', $event)"
    step="1"
    :headers="headers"
    :items="aspects"
    item-key="id"
    class="elevation-1"
    data-app
    show-select
  >
    >
    <template #[`item.explanation`]="props">
      <v-textarea v-model="props.item.explanation"></v-textarea>
    </template>
  </v-data-table>
</template>

<script>
import { axiosInstance } from '../../lib/axiosInstance'

export default {
  props: ['selectedAspects'],
  name: 'AspectLijstStudenten',
  data () {
    return {
      aspects: [],
      aspectRatings: [],
      dialog: false,
      headers: [
        { text: 'Titel', value: 'title' },
        { text: 'Korte Beschrijving', value: 'short_description' },
        { text: 'Beschrijving', value: 'description' },
        { text: 'Jou geschreven toelichting', value: 'explanation' }
      ],
      aspectList: {
        title: '',
        short_description: '',
        description: '',
        external_url: '',
        rating_ids: []
      }
    }
  },

  mounted () {
    axiosInstance
      .get('api/v1/aspects')
      .then(response => (this.aspects = response.data))
    axiosInstance
      .get('api/v1/ratings')
      .then(response => (this.aspectRatings = response.data))
  },
  methods: {
    submitForm () {
      axiosInstance
        .post('api/v1/users/1/posts', this.values)
        // .patch(`api/v1/aspects/${this.aspects.id}`)
        .then(response => (this.values = response.data))
        .catch(function (error) {
          if (error.response) {
            // De post request is gemaakt en de server gaf in de terminal een status code aan

            console.log(error.response.data)
            console.log('render error', error.response.status)
            alert('Je bent momenteel niet ingelogd').console.log('je bent momenteel niet ingelogd', error.response.headers)
          } else if (error.request) {
            // Request is verzonden, echter geen reactie terug
            alert('De website is momenteel niet beschikbaar').console.log('De website is momenteel niet beschikbaar', error.request)
          } else {
            // Iets in de request heeft voor een error gezorgd
            alert('Er is iets mis gegaan met het versturen van de data').console.log('Er is iets mis gegaan met het versturen van de data', error.message)
          }
          console.log(error.config)
        })
    }
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

.v-card {
  margin: 15px;
  border-top-left-radius: 15px !important;
  border-top-right-radius: 15px !important;
}

.v-icon {
  z-index: auto;
}
</style>
