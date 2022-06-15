<template>
  <!-- Data Tabel -->
  <v-data-table
    :headers="headers"
    :items="ratings"
    sort-by="title"
    class="elevation-1"
    data-app
  >
    <!-- De Header van het Tabel -->
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

        <!-- Form Dialog -->
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <!-- New Item Button -->
          <template #activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              New Item
            </v-btn>
          </template>

          <!-- V-card Form -->
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.title"
                      label="Rating Title"
                    />
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.short_description"
                      label="Korte Beschrijving"
                    />
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.description"
                      label="Beschrijving"
                    />
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <!-- V-card acties -->
            <v-card-actions>
              <v-spacer />
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="updateForm"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <!-- Items bewerken/verwijderen knoppen -->
    <template #[`item.actions`]="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import { axiosInstance } from '../../lib/axiosInstance'

export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      { text: 'Titel', value: 'title' },
      { text: 'Korte Beschrijving', value: 'short_description' },
      { text: 'Beschrijving', value: 'description' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    ratings: [],
    desserts: [],
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
  }),

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
    },

    updateForm () {
      if (this.editedIndex > -1) {
        axiosInstance.patch(`api/v1/ratings/${this.ratings[this.editedIndex].id}`, this.editedItem)
          .then((response) => {
          // Perform Success Action
            console.log(response)
          })
          .catch((error) => {
          // error.response.status Check status code
            console.log(error)
          })
        Object.assign(this.ratings[this.editedIndex], this.editedItem)
      } else {
        this.ratings.push(this.editedItem)
      }
      this.close()
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
  border-top-left-radius: 15px !important;
  border-top-right-radius: 15px !important;
}

.v-icon {
  z-index: auto;
}
</style>
