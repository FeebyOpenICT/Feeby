<template className="container">
  <div id="app">
    <HeaderCom/>
    <v-app>
      <v-container>
        <v-form ref="form" lazy-validation v-on:submit.prevent="submitForm">
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
                       color="primary"
                       @click="e1 = 2"
                       :disabled="!valid"
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
                        Sleep je bestanden vanaf jou computer hierin.
                      </p>
                    </v-row>
                    <v-file-input
                      v-model="form.uploadFiles"
                      multiple
                      show-size
                      truncate-length="15"
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
                <div class="checkBoxContainer" id="knowledge">
                  <div id="aspectCheck"
                  >
                    <v-checkbox v-model="form.aspects" type="button" class="selectBox" @click="isHidden = !isHidden"></v-checkbox>
                    <p class="aspect" style="color: white;"><strong>Juiste kennis opdoen</strong></p>
                  </div>
                  <v-textarea class="textField"
                              v-model="form.aspects"
                              id="aspectDescription"
                              v-if="!isHidden"
                              counter
                              type="text"
                              placeholder="Schrijf hier je toelichting over dit aspect..."
                  />
                  <v-btn class="btn"
                       @click="e1=2"
                       style="background-color: white;
                       white; color: #0079CF;
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
                  <v-checkbox style="color: white;" v-model="form.aspects" type="button" class="selectBox" disabled></v-checkbox>
                  <p class="aspect" style="color: white;"><strong>Juiste kennis opdoen</strong></p>
                  <v-text-field class="textField"
                              style="background-color: white"
                              v-model="form.aspects"
                              id="aspectDescription"
                              disabled
                  />
                </div>
                <v-btn class="btn-back"
                       @click="e1=3"
                       style="background-color:
                       white; color: #0079CF;
                       border-style: solid;
                       border-color: #0079CF"
                >
                  Ga terug
                </v-btn>
                <div className="form-buttons">
                  <button className="btn btn-primary">Versturen</button>
                </div>
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
// import UploadBox from '~/components/PostrevisionComponents/uploadBox'
// import HeaderCom from './HeaderCom.vue'
// import FooterCom from './FooterCom.vue'
export default {
  name: 'RevisionPage',
  data: () => ({
    visible: true,
    isHidden: true,
    e1: 1,
    user: '',
    dragover: false,
    titleRules: [
      v => !!v || 'Titel is verplicht',
      v => (v && v.length <= 74) || 'Titel mag niet meer dan 75 characters hebben'
    ],
    descriptionRules: [
      v => !!v || 'Beschrijving is verplicht'
    ],
    form: {
      title: '',
      description: '',
      aspects: '',
      uploadedFiles: []
    }
  }),
  mounted () {
    axiosInstance
      .get('/api/v1/users/1/self')
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
<style>
.formField {
  max-width: 75%;
}

</style>
