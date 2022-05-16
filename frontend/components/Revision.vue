<template className="container">
  <div id="app">
<v-form ref="form" lazy-validation>

  <v-stepper v-model="e1" style="background-color: #F3F3F3">
    <v-stepper-header style="background-color: #0079CF">
      <v-stepper-step
        :complete="e1 > 1"
        step="1"
        style="font-weight: bold"
      >
        Titel en beschrijving
      </v-stepper-step>

      <v-divider style="background-color: white"></v-divider>

      <v-stepper-step
        :complete="e1 > 2"
        step="2"
        style="background-color: #0079CF; font-weight: bold"
      >
        Bestanden uploaden
      </v-stepper-step>

      <v-divider style="background-color: white"></v-divider>

      <v-stepper-step step="3"
       style="background-color: #0079CF; font-weight: bold"
      >
        Aspecten selecteren
      </v-stepper-step>

      <v-divider style="background-color: white"></v-divider>

      <v-stepper-step step="4"
       style="background-color: #0079CF; font-weight: bold"
      >
        Versturen
      </v-stepper-step>
    </v-stepper-header>

    <v-stepper-items v-model="valid">
      <v-stepper-content step="1" >
          <v-card-title><strong>Vul titel in</strong></v-card-title>
          <v-text-field
                      maxlength="75"
                      placeholder="Schrijf hier de titel van je post..."
                      v-model="form.title"
                      outlined
                      color="grey"
                      filled
                      :rules="[v => !!v || 'Titel is verplicht.']"
                      required>

          </v-text-field>
        <v-card-title><strong>Vul beschrijving in</strong></v-card-title>
          <v-text-field
            type="text"
            className="formField"
            maxlength="75"
            placeholder="Schrijf hier de beschrijving van je post..."
            v-model="form.description"
            outlined
            color="grey"
            filled
            :rules="[v => !!v || 'Beschrijving is verplicht.']"
            required>
        </v-text-field>
        <v-btn class="btn"
          color="primary"
          @click="e1 = 2"
          style="background-color: #0079CF; color: white"
          :disabled="!valid"
        >
          Continue
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="2">
        <v-card
          class="mb-12"
          color="grey lighten-1"
        >
          <div className="form-group">
            <UploadBox />
          </div>
        </v-card>
        <v-btn class="btn"
               @click="e1 = 1"
               style="background-color: #0079CF; color: white"
        >
          Ga terug
        </v-btn>
        <v-btn class="btn"
               color="primary"
               @click="e1 = 3"
               style="background-color: #0079CF; color: white"
        >
          Ga verder
        </v-btn>
      </v-stepper-content>
      <v-stepper-content step="3">
        <v-card
          class="mb-12"
          color="grey lighten-1"
        ></v-card>
        <v-btn class="btn"
               @click="e1=2"
               style="background-color: #0079CF; color: white"
        >
          Ga terug
        </v-btn>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</v-form>
  </div>

</template>
<script>
import { axiosInstance } from '../lib/axiosInstance'
import UploadBox from '~/components/PostrevisionComponents/uploadBox'
// import HeaderCom from './HeaderCom.vue'
// import FooterCom from './FooterCom.vue'
export default {
  components: { UploadBox },
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
      .get('/api/v1/users/1/self')
      .then(response => (this.user = response.data))
  },
  methods: {
    continue () {
      this.$refs.form.continue()
    },

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
<style>
.v-text-field--outlined fieldset {
  color: #0079CF !important;
  background-color: white;
  border-width: 2px;
}
</style>
