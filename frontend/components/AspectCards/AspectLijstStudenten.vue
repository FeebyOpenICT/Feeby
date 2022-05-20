<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <!-- Data Tabel -->
  <v-data-table
    :headers="headers"
    :items="aspects"
    item-key="title"
    class="elevation-1"
    data-app
    show-select
  >
    <!-- De Header van het Tabel -->
    <template #top>
      <v-toolbar
        flat
      >
        <!-- TItle bar from Toolbar -->
        <v-toolbar-title>Mijn Aspecten</v-toolbar-title>
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
          <!-- V-card Form -->
          <v-card>

            <!-- V-card Text Form -->
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
                      label="Aspect Title"
                      counter
                      maxlength="255"
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
                      counter
                      maxlength="255"
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
                      counter
                      maxlength="1000"
                    />
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.external_url"
                      label="Link"
                      counter
                      maxlength="2000"
                    />
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="editedItem.ratings"
                      :items="aspectRatings"
                      label="Rating"
                      multiple
                      counter
                      item-text="title"
                      item-value="id"
                      chips
                    />
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <!-- V-card acties -->
            <v-card-actions>
              <v-spacer />
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
  name: 'AspectLijstStudenten',
  data: () => ({
    dialog: false,
    headers: [
      { text: 'Titel', value: 'title' },
      { text: 'Korte Beschrijving', value: 'short_description' },
      { text: 'Beschrijving', value: 'description' }
    ],
    aspects: [],
    aspectRatings: [],
    editedIndex: -1,
    editedItem: {
      title: '',
      short_description: '',
      description: '',
      external_url: '',
      selected: [],
      rating_ids: ''
    },
    defaultItem: {
      title: '',
      short_description: '',
      description: '',
      external_url: '',
      selected: [],
      rating_ids: ''
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
