<template className="container">
  <div id="app">
    <HeaderCom />
    <v-app>
      <v-container>
        <v-form ref="form" lazy-validation v-on:submit.prevent="submitForm" v-model="valid">
          <v-stepper v-model="e1" style="background-color: #F3F3F3"><v-stepper-header style="background-color: #0079CF">
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

            <v-stepper-step
              :complete="e1 > 3"
              step="3"
              style="background-color: #0079CF; font-weight: bold"
            >
              Aspecten selecteren
            </v-stepper-step>

            <v-divider style="background-color: white"></v-divider>

            <v-stepper-step
              :complete="e1 > 4"
              step="4"
              style="background-color: #0079CF; font-weight: bold"
            >
              Versturen
            </v-stepper-step>
          </v-stepper-header>

            <v-stepper-items>
              <v-stepper-content step="1" v-on:submit.prevent="valid">
                <v-card-title><strong>Vul titel in</strong></v-card-title>
                <v-text-field
                  background-color="white"
                  type="text"
                  class="formField"
                  maxlength="75"
                  v-model="form.title"
                  outlined
                  label="Schrijf hier de titel van je post..."
                  filled
                  :rules="titleRules"
                  required>

                </v-text-field>
                <v-card-title><strong>Vul beschrijving in</strong></v-card-title>
                <v-textarea
                  background-color="white"
                  type="text"
                  class="formField"
                  maxlength="500"
                  label="Schrijf hier de beschrijving van je post..."
                  v-model="form.description"
                  outlined
                  :rules="descriptionRules"
                  required>
                </v-textarea>
                <v-btn class="btn"
                       :disabled="!valid"
                       color="primary"
                       @click="e1 = 2"
                       style="background-color: #0079CF; color: white"
                >
                  Continue
                </v-btn>
              </v-stepper-content>

              <v-stepper-content step="2"
                                 align="center"
              >
                <v-card justify="center"
                        align="center"
                        @drop.prevent="dragover = false"
                        @dragover.prevent="dragover = true"
                        @dragenter.prevent="dragover = true"
                        @dragleave.prevent="dragover = false"
                        style="background-color: #0079CF; max-width: 50%"
                >
                  <v-card-text
                  >
                    <v-row class="d-flex flex-column" dense align="center" justify="center">
                      <v-icon class="mt-3" size="70" style="color:white">mdi-cloud-upload</v-icon>
                      <p class="d-flex flex-column" dense align="center" justify="center" style="color: white">
                        Sleep of klik om uw bestanden te uploaden.
                      </p>
                    </v-row>
                    <v-file-input
                      v-model="form.uploadFiles"
                      chips
                      counter
                      multiple
                      truncate-length="50"
                    />
                  </v-card-text>
                  <v-card-actions></v-card-actions>
                  <v-spacer></v-spacer>
                </v-card>
                <div class="buttonContainer" style="margin-top: 20px">
                  <v-btn class="btn"
                         @click="e1=1"
                         style="background-color: white;
                       color: #0079CF;
                       border-style: solid;
                       border-color: #0079CF"
                  >
                    Ga terug
                  </v-btn>
                  <v-btn class="btn-back"
                         color="primary"
                         @click="e1 = 3"
                         style="background-color: #0079CF; color: white"
                  >
                    Continue
                  </v-btn>
                </div>
              </v-stepper-content>
              <v-stepper-content step="3">
                <v-data-table
                  :items="aspects"
                  :value="selectedAspects"
                  @input="$emit('update:selectedAspects', $event)"
                  :headers="headers"
                  v-model="form.aspects"
                  item-key="id"
                  class="elevation-1"
                  data-app
                  show-select
                ><template #[`item.explanation`]="props">
                  <v-textarea v-model="props.item.explanation" outlined></v-textarea>
                </template>
                  <template #[`item.selectRating`]="props">
                    <div class="text-center mt-5">
                      <v-rating v-model="props.item.selectedRating"
                                color="primary"
                                background-color="grey darken-1"
                                empty-icon="$ratingFull"
                                half-increments
                                hover
                                large
                      ></v-rating>
                    </div>
                  </template>
                </v-data-table>
                <div classname="buttons" align="center" justify="center">
                  <v-btn class="btn"
                         @click="e1=2"
                         style="background-color: white; margin: 15px;
                       color: #0079CF;
                       border-style: solid;
                       border-color: #0079CF"
                  >
                    Ga terug
                  </v-btn>
                  <v-btn class="btn"
                         color="primary"
                         @click="e1 = 4"
                         style="background-color: #0079CF; color: white"
                  >Inzien
                  </v-btn>
                </div>

              </v-stepper-content>
              <v-stepper-content step="4">
                <v-card-title><strong>Titel</strong></v-card-title>
                <v-text-field
                  background-color="white"
                  type="text"
                  class="formField"
                  maxlength="75"
                  placeholder="Schrijf hier de titel van je post..."
                  v-model="form.title"
                  outlined
                  color="grey"
                  :rules="[v => !!v || 'Titel is verplicht.']"
                  required
                  disabled
                >
                </v-text-field>
                <v-card-title><strong>Beschrijving</strong></v-card-title>
                <v-text-field
                  background-color="white"
                  type="text"
                  class="formField"
                  outlined
                  v-model="form.description"
                  disabled
                >
                </v-text-field>
                <v-file-input
                  v-model="form.uploadFiles"
                  multiple
                  show-size
                  truncate-length="15"
                  disabled
                />
                <div style="background-color: #0079CF;  max-width: 75%">
                </div>
                <v-data-table
                  :value="selectedAspects"
                  @input="$emit('update:selectedAspects', $event)"
                  :headers="headers"
                  :items="aspects"
                  v-model="form.aspects"
                  item-key="id"
                  class="elevation-1"
                  data-app
                  disabled
                >
                  <template #[`item.selectRating`]="props">
                  <div class="text-center mt-5">
                    <v-rating v-model="props.item.selectedRating"
                      color="primary"
                      background-color="grey darken-1"
                      empty-icon="$ratingFull"
                      half-increments
                      hover
                      large
                      readonly
                    ></v-rating>
                  </div>
                </template>
                </v-data-table>
                <v-btn class="btn-back"
                       @click="e1=3"
                       style="
                       background-color: white;
                       color: #0079CF;
                       border-style: solid;
                       border-color: #0079CF"
                >
                  Ga terug
                </v-btn>
                <v-btn classname="form-buttons"
                       style="
                       background-color: #0079CF;
                       color: white;
                       border-style: solid;
                       border-color: #0079CF">
                  <button className="btn btn-primary">VERSTUREN</button>
                </v-btn>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-form>
      </v-container>
    </v-app>
  </div>

</template>
<script>
import { axiosInstance } from '../lib/axiosInstance'
import HeaderCom from './HeaderCom.vue'
// import UploadBox from '~/components/PostrevisionComponents/uploadBox'
// import FooterCom from './FooterCom.vue'
export default {
  components: { HeaderCom },
  name: 'ProductPage',
  data () {
    return {
      dialog: false,
      selectedAspects: '',
      visible: true,
      isHidden: true,
      valid: true,
      e1: 1,
      user: '',
      aspects: [],
      selectedRating: null,
      aspectRatings: [],
      dragover: false,
      titleRules: [
        v => !!v || 'Titel is verplicht',
        v => (v && v.length <= 74) || 'Titel mag niet meer dan 75 characters hebben'
      ],
      descriptionRules: [
        v => !!v || 'Beschrijving is verplicht'
      ],
      form: [{
        post_id: '',
        title: '',
        description: '',
        uploadedFiles: []
      }],
      aspectList: {
        title: '',
        short_description: '',
        description: '',
        aspects: [],
        external_url: '',
        rating_ids: []
      },
      headers: [
        { text: 'Titel', value: 'title' },
        { text: 'Korte Beschrijving', value: 'short_description' },
        { text: 'Beschrijving', value: 'description' },
        { text: 'Jou geschreven toelichting', value: 'explanation' },
        { text: 'rating', value: 'selectRating' }
      ]
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
        .post('api/v1/users/1/posts', this.form)
        // .patch(`api/v1/aspects/${this.aspects.id}`)
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
    },

    selectRating (item) {
      this.selectedRating = Object.assign({}, item)
      this.dialog = true
    }
  }
}

</script>
<style>
.formField {
  max-width: 75%;
}

</style>
