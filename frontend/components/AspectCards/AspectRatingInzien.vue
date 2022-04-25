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
      :items="desserts"
      hide-default-footer
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

          <!-- Dialog Update Pop-Up -->
          <v-overlay
            v-model="overlay"
            data-app
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
                  @click="overlay = false"
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
          @click="overlay = !overlay"
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
      absolute: true,
      headers: [
        { text: 'Titel', value: 'title' },
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
      },
      desserts: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3
        },
        {
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0
        },
        {
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3
        },
        {
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9
        },
        {
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0
        },
        {
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0
        },
        {
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5
        },
        {
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9
        },
        {
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7
        }
      ]
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

.v-card {
  margin: 15px;
  border-top-left-radius: 15px !important;
  border-top-right-radius: 15px !important;
}

.v-icon {
  z-index: auto;
}
</style>
