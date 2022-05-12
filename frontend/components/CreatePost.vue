<template className="container">
  <div>
    <HeaderCom/>
    <div className="postPage">
      <h1 className="pageTitle">Product inleveren</h1>
      <form v-on:submit.prevent="submitForm">
        <div className="form-group">
          <h2><strong>Titel</strong></h2>
          <v-textarea type="text"
                      className="formField"
                      counter
                      maxlength="2000"
                      id="title"
                      placeholder="Schrijf hier de titel van je post..."
                      v-model="form.title"
                      required>
          </v-textarea>
        </div>
        <div className="form-group">
          <h2><strong>Toelichting</strong></h2>
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
        <!--          <div class="aspect-group">-->
        <!--          <AspectKnowledge v-model="form.aspects" />-->
        <!--          </div>-->
        <div className="form-buttons">
          <button className="btn btn-primary">Submit</button>
        </div>
      </form>
    </div>
<!--    <FooterCom/>-->
  </div>
</template>

<script>

import { axiosInstance } from '../lib/axiosInstance'
import HeaderCom from './HeaderCom.vue'
// import FooterCom from './FooterCom.vue'

export default {
  name: 'CreatePost',
  components: { HeaderCom },
  data () {
    return {
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
