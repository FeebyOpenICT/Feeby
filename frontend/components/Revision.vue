<template className="container">
  <div id="app">
<form v-on:submit.prevent="submitForm">
  <v-stepper v-model="e1">
    <v-stepper-header>
      <v-stepper-step
        :complete="e1 > 1"
        step="1"
      >
        Titel en beschrijving
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step
        :complete="e1 > 2"
        step="2"
      >
        Bestanden uploaden
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="3">
        Aspecten selecteren
      </v-stepper-step>
    </v-stepper-header>

    <v-stepper-items>
      <v-stepper-content step="1">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        >
          <h2><strong>Vul titel in</strong></h2>
          <v-textarea type="text"
                      className="formField"
                      maxlength="2000"
                      placeholder="Schrijf hier de titel van je post..."
                      v-model="form.title"
                      required>
          </v-textarea>
        </v-card>
        <v-btn
          color="primary"
          @click="e1 = 2"
        >
          Continue
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="2">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        >
          <div className="form-group">
            <h2><strong>Vul Toelichting in</strong></h2>
            <v-textarea type="text"
                        className="formField"
                        counter
                        maxlength="2000"
                        id="Description"
                        placeholder="Schrijf hier de beschrijving van je post..."
                        v-model="form.description"
                        required>
            </v-textarea>
          </div>
        </v-card>

        <v-btn
          @click="e1 = 1"
        >
          Ga terug
        </v-btn>
        <v-btn
          color="primary"
          @click="e1 = 3"
        >
          Continue
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="3">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        ></v-card>
        <v-btn
          @click="e1 = 2"
        >
          Ga terug
        </v-btn>

        <div className="stepper-buttons">
          <button className="btn btn-primary">Submit</button>
        </div>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</form>
  </div>

</template>
<script>
import { axiosInstance } from '../lib/axiosInstance'
// import HeaderCom from './HeaderCom.vue'
// import FooterCom from './FooterCom.vue'
export default {
  name: 'RevisionPage',
  data () {
    return {
      e1: 1,
      user: '',
      form: {
        title: '',
        description: ''
      }
    }
  },
  mounted () {
    axiosInstance
      .get('/api/v1/users/self')
      .then(response => (this.user = response.data))
  },
  methods: {
    submitForm () {
      axiosInstance
        .post('api/v1/users/1/posts', this.form)
        .then(response => (this.form = response.data))
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
