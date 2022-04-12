<template>
  <div id="postcard">
    <v-card
      v-for="card in orderedCards"
      :key="card.id"
      class="postcard"
    >
      <div class="cardheader">
        <v-card-title>{{ card.title }}</v-card-title>
        <v-card-subtitle>
          {{ card.time_created }}
        </v-card-subtitle>
      </div>
      <v-card-text id="body">
        {{ card.description }}
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import _ from 'lodash'
import '../style/style.css'
import { axiosInstance } from '../lib/axiosInstance'

export default {
  name: 'CardCom',
  data () {
    return {
      cards: null
    }
  },
  computed: {
    orderedCards () {
      return _.orderBy(this.cards, 'time_created')
    }
  },
  mounted () {
    axiosInstance
      .get('/api/v1/posts/self')
      .then(response => (this.cards = response.data))
      .catch(error => console.log(error))
  }
}
</script>

<style scoped>
.postcard{
    width: 90vw;
    max-width: 90vw;
    min-width: 30vw;
    height: 25vh;
    min-height: 10vw;
    max-height: 25vw;
    overflow: hidden;
    position: relative;
    left: 5vw;
    border-style: hidden solid solid;
    border-width: 1px;
    border-color: black;
    margin-bottom: 2vw;
    margin-top: 2vw;
  }

.cardheader{
    background-color: var(--blue);
    color: white;
}
</style>
