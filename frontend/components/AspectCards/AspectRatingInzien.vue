<template>
  <v-card
    class="mx-auto"
    max-width="600"
    max-height="700"
    tile
    outlined
    elevation="2"
    border
  >
    <!-- Vuetify Data Table Component -->
    <v-data-table
      :headers="headers"
      :items="ratings"
      sort-by="title"
      class="elevation-1"
    >
      <template #top>
        <v-toolbar
          flat
        >
          <v-toolbar-title>Mijn Ratings</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          />
          <v-spacer />

          <!-- Aspect Rating Aanmaken Overlay -->
          <!-- <v-dialog v-model="overlay" class="overlay"> -->
          <!-- New Item Button -->
          <!-- <template #activator="{ on, attrs }">
              <v-btn
                color="#0079CF"
                text-color="white"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
              >
                New Item
              </v-btn>
            </template> -->

          <!-- Aspect Rating Aanmaken Card -->
          <!-- <v-card>
              <AspectRatingAanmaken />
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="blue darken-1"
                  text
                  @click="close"
                >
                  Close
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog> -->

          <!-- Dialog Update Pop-Up -->
          <v-overlay
            v-model="dialog"
            :absolute="absolute"
            data-app
            max-width="80%"
          >
            <!-- Update Items -->
            <v-card light class="RatingCard">
              <AspectRatingUpdaten />
              <!-- Close Button -->
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="blue darken-1"
                  text
                  @click="dialog = false"
                >
                  Cancel
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-overlay>
        </v-toolbar>
      </template>

      <!-- Update Button -->
      <template #[`item.actions`]>
        <v-icon
          small
          class="mr-2"
          @click="dialog = !dialog"
        >
          mdi-pencil
        </v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import AspectRatingUpdaten from './AspectRatingUpdaten.vue'
import { axiosInstance } from '~/lib/axiosInstance'
export default {
  name: 'AspectRatingInzien',
  components: { AspectRatingUpdaten },
  data () {
    return {
      overlay: false,
      dialog: false,
      absolute: true,
      headers: [
        {
          text: 'Titel',
          align: 'start',
          value: 'title'
        },
        { text: 'Korte Beschrijving', value: 'short_description' },
        { text: 'Beschrijving', value: 'description' },
        { text: 'Acties', value: 'actions', sortable: false }
      ],
      ratings: [],
      editedIndex: -1,
      editedItem: {
        title: '',
        short_description: '',
        description: ''
      },
      defaultItem: {
        title: '',
        short_description: '',
        description: ''
      }
    }
  },
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    }
  },
  watch: {
    dialog (val) {
      val || this.close()
    }
  },
  mounted () {
    axiosInstance
      .get('api/v1/ratings/')
      .then(response => (this.ratings = response.data))
      .catch(error => console.log(error))
  },
  methods: {
    editItem (item) {
      this.editedIndex = this.ratings.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    }
  }
}
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

.v-card{
  margin: 15px;
  border-top-left-radius: 15px !important;
  border-top-right-radius: 15px !important;
}
</style>
