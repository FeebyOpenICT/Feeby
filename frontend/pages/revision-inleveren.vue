<template>
  <div id="app">
    <v-form ref="form" lazy-validation v-on:submit.prevent="submitForm" v-model="valid" class="pa-2">
      <!-- HEADER + STEPPERS-->
      <v-stepper v-model="e1">
        <v-stepper-header>
          <v-stepper-step
            color="primary"
            :complete="e1 > 1"
            step="1"
          >
            Beroepsproduct
          </v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step
            color="primary"
            :complete="e1 > 2"
            step="2"
          >
            Bestanden
          </v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step
            color="primary"
            :complete="e1 > 3"
            step="3"
          >
            Nulmeting
          </v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>

          <!--          STAP 1-->
          <v-stepper-content step="1" v-on:submit.prevent="valid">
            <v-card>
              <v-card-title>Titel</v-card-title>
              <v-card-text>
                <v-text-field
                  background-color="white"
                  type="text"
                  class="formField"
                  maxlength="75"
                  v-model="form.title"
                  outlined
                  filled
                  :rules="titleRules"
                  required
                />
              </v-card-text>
              <v-card-title>Beschrijving</v-card-title>
              <v-card-text>
                <v-textarea
                  background-color="white"
                  type="text"
                  class="formField"
                  maxlength="500"
                  v-model="form.description"
                  outlined
                  :rules="descriptionRules"
                  required
                />
              </v-card-text>
              <v-card-actions>
                <v-btn
                  :disabled="!valid"
                  color="primary"
                  @click="e1 = 2"
                >
                  Verder
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>

          <!-- STAP 2-->
          <v-stepper-content step="2"
          >
            <v-card>
              <v-card-title>Bestanden</v-card-title>
              <v-card-text>
                <v-file-input>
                  chips
                  counter
                  multiple
                  truncate-length="50"
                </v-file-input>
              </v-card-text>
              <v-card-title>Beschrijving</v-card-title>
              <v-card-text>
                <v-textarea
                  background-color="white"
                  label="Toelichting geselecteerde bestanden"
                  type="text"
                  class="formField"
                  maxlength="500"
                  v-model="form.revision.description"
                  outlined
                  :rules="descriptionRules"
                  required>
                </v-textarea>
              </v-card-text>
              <v-card-actions>
                <v-btn
                  @click="e1=1"
                >
                  Terug
                </v-btn>
                <v-btn
                  color="primary"
                  @click="e1 = 3"
                >
                  Verder
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
          <!-- STAP 3-->
          <v-stepper-content step="3" class="pa-5">
            <v-card>
              <v-data-table
                :items="aspects"
                :headers="headers"
                item-key="id"
                show-select
              >
                <template #[`item.explanation`]="props">
                  <v-textarea v-model="props.item.explanation" outlined class="pa-5"></v-textarea>
                </template>
              </v-data-table>
              <v-card-actions>
                <v-btn
                  @click="e1=2"
                >
                  Terug
                </v-btn>
                <v-btn
                  v-on:click.prevent="submitForm()" class="btn btn-primary"
                  color="primary"
                >
                  Verstuur
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-form>
  </div>
</template>
<script>
export default {
  name: 'revision-inleveren',
  data() {
    return {
      aspects: [],
      dialog: false,
      selectedAspects: '',
      visible: true,
      isHidden: true,
      valid: true,
      e1: 1,
      user: [],
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
        revision: {
          description: ''
        }
      },
      headers: [
        {text: 'Titel', value: 'title'},
        {text: 'Korte Beschrijving', value: 'short_description'},
        {text: 'Beschrijving', value: 'description'},
        {text: 'Jou geschreven toelichting', value: 'explanation'},
        {text: 'rating', value: 'selectRating'}
      ]
    }
  },
  async fetch() {
    this.aspects = await this.$axios.$get('aspects')
    console.log(this.aspects)
  },
  methods: {
    submitForm() {
      this.form = this.$axios.$post('users/1/posts', this.form)
    }
  }
}

</script>
<style scoped>
.btn {
  margin: 15px;
}
</style>
