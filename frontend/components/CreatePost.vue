<template class="container">
  <div>
    <HeaderCom />
    <div class="postPage">
      <h1 class="pageTitle">Product inleveren</h1>
      <form v-on:submit.prevent="submitForm">
        <div class="form-group">
          <h2><strong>Titel</strong></h2>
          <v-textarea type="text"
                 class="formField"
                 counter
                 maxlength="2000"
                 id="title"
                 placeholder="Schrijf hier de titel van je post..."
                 v-model="form.title"
                 required>
          </v-textarea>
        </div>
        <div class="form-group">
          <h2><strong>Toelichting</strong></h2>
          <v-textarea type="text"
                 class="formField"
                 counter
                 maxlength="2000"
                 id="Description"
                 placeholder="Schrijf hier de beschrijving van je post..."
                 v-model="form.description"
                 required>
        </v-textarea>
        </div>
<!--          <div class="aspect-group">-->
<!--          <AspectKnowledge v-model="form.aspects" />-->
<!--          </div>-->
        <div class="form-buttons">
          <button class="btn btn-primary">Submit</button>
        </div>
      </form>
  </div>
    <FooterCom />
  </div>
</template>

<script>
import { axiosInstance } from '../lib/axiosInstance'
import HeaderCom from './HeaderCom.vue'
import FooterCom from './FooterCom.vue'
export default {
  name: 'CreatePost',
  components: { HeaderCom, FooterCom },
  data () {
    return {
      form: {
        title: '',
        description: '',
        aspects: ''
      }
    }
  },
  methods: {
    submitForm () {
      axiosInstance
        .post('api/v1/posts', this.form)
        .then(response => (this.form = response.data))
        .catch(function (error) {
          if (error.response) {
            // De post request is gemaakt en de server gaf in de terminal een status code aan

            console.log(error.response.data)
            console.log('render error', error.response.status)
            console.log('je bent momenteel niet ingelogd', error.response.headers)
          } else if (error.request) {
            // Request is verzonden, echter geen reactie terug
            console.log('Er is iets fout gegaan', error.request)
          } else {
            // Iets in de request heeft voor een error gezorgd
            console.log('Er is iets mis gegaan met het versturen van de data', error.message)
          }
          console.log(error.config)
        })
    }
  }
}
</script>
