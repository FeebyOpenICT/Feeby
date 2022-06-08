<template>
  <v-card v-model="aspectTabel">
    <!-- Data Tabel -->
    <v-data-table
      :headers="headers"
      :items="aspects"
      sort-by="title"
      class="elevation-1"
      data-app
      temporary
    >
      <template #[`item.ratings`]="{ item }">
        <td>{{ getRatingNames(item.ratings) }}</td>
      </template>

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
            max-width="80%"
            max-height="80%"
          >
            <!-- V-card Form -->
            <v-card>
              <!-- V-card Title Form -->
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

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
                        required
                      />
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-textarea
                        v-model="editedItem.short_description"
                        class="textField"
                        label="Korte Beschrijving"
                        counter
                        maxlength="255"
                        required
                      />
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-textarea
                        v-model="editedItem.description"
                        class="textField"
                        label="Beschrijving"
                        counter
                        maxlength="1000"
                        required
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
                        required
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
                        chips
                        item-text="title"
                        item-value="id"
                        required
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
  </v-card>
</template>

<script>
import { axiosInstance } from '../../lib/axiosInstance'

export default {
  name: 'AspectInzien',
  data: () => ({
    dialog: null,
    aspectTabel: null,
    headers: [
      { text: 'Titel', value: 'title' },
      { text: 'Korte Beschrijving', value: 'short_description' },
      { text: 'Beschrijving', value: 'description' },
      { text: 'Link', value: 'external_url' },
      { text: 'Ratings', value: 'ratings' },
      { text: 'Actions', value: 'actions', sortable: false }
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

  async mounted () {
    try {
      const response = await axiosInstance.get('api/v1/aspects')
      this.aspects = response.data
      const resp = await axiosInstance.get('api/v1/ratings')
      this.aspectRatings = resp.data
    } catch (err) {
      // eslint-disable-next-line no-console
      console.log(err)
    }
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

    getRatingNames: (ratings) => {
      return ratings.map(rating => rating.title).join(', ').toString()
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
  border-top-left-radius: 15px !important;
  border-top-right-radius: 15px !important;
}

.v-icon {
  z-index: auto;
}
</style>
