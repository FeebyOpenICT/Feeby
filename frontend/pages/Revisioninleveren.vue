<template className="container">
  <RevisionPage />
</template>

<script>

import { axiosInstance } from '../lib/axiosInstance'
import RevisionPage from '~/components/Revision.vue'
// import HeaderCom from './HeaderCom.vue'
// import FooterCom from './FooterCom.vue'

export default {
  name: 'BeroepsproductInleveren',
  components: { RevisionPage },
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
        .post('api/v1/users/1/posts/1/revisions', this.form)
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
