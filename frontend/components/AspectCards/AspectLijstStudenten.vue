<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <!-- Data Tabel -->
  <v-data-table
    v-model="message"
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
    <template>
      <v-text-field
        v-model.trim="selectAspect"></v-text-field>
    </template>
  </v-data-table>
</template>

<script>
import Vuex from 'vuex'
import { axiosInstance } from '../../lib/axiosInstance'

export default new Vuex.Store({
  state: {
    selectAspect: ''
  },

  props: ['selectedAspects'],
  name: 'AspectLijstStudenten',
  data: () => ({
    dialog: false,
    headers: [
      { text: 'Titel', value: 'title' },
      { text: 'Korte Beschrijving', value: 'short_description' },
      { text: 'Beschrijving', value: 'description' },
      { text: 'Jou geschreven toelichting', value: 'explanation' }

    ],
    aspects: [],
    aspectRatings: [],
    editedIndex: -1,
    editedItem: {
      title: '',
      short_description: '',
      description: '',
      external_url: '',
      rating_ids: ''
    },
    defaultItem: {
      title: '',
      short_description: '',
      description: '',
      external_url: '',
      rating_ids: ''
    }
  }),

  computed: {
    selectAspect: {
      get () {
        return this.$store.state.selectAspect
      },
      set (newValue) {
        this.selectAspect = newValue
      }
    }
  },

  watch: {
    dialog (val) {
      val || this.close()
    }
  },

  mounted () {
    axiosInstance
      .get('api/v1/aspects')
      .then(response => (this.aspects = response.data), JSON.stringify([this.aspects]))
    axiosInstance
      .get('api/v1/ratings')
      .then(response => (this.aspectRatings = response.data))
  },

  methods: {
    editItem (item) {
      this.editedIndex = this.aspects.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    updateForm () {
      if (this.editedIndex > -1) {
        axiosInstance.patch(`api/v1/aspects/${this.aspects[this.editedIndex].id}`, this.editedItem)
        Object.assign(this.aspects[this.editedIndex], this.editedItem)
      } else {
        this.aspects.push(this.editedItem)
      }
      this.close()
    }
  }
})

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
