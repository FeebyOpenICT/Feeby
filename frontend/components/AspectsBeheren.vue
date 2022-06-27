<template>
  <v-card>
    <v-card-title>Aspects</v-card-title>
    <v-card-text>
      <!-- Data Tabel -->
      <v-data-table :headers="headers" :items="aspects" sort-by="title">
        <!-- Ratings In Chips In Table -->
        <template #[`item.ratings`]="{ item }">
          <v-chip-group>
            <v-chip v-for="rating in item.ratings" :key="rating">{{
                rating.title
              }}
            </v-chip>
          </v-chip-group>
        </template>

        <template #top>
          <!-- Edit Item Dialog -->
          <v-dialog
            @click:outside="close"
            v-model="edit_aspect_dialog"
            max-width="800"
            persistent
          >
            <!-- V-card Form -->
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

              <!-- V-card text -->
              <v-card-text>
                <AspectsForm
                  :default_ratings="edit_aspect.default_ratings"
                  :title.sync="edit_aspect.title"
                  :short_description.sync="edit_aspect.short_description"
                  :description.sync="edit_aspect.description"
                  :external_url.sync="edit_aspect.external_url"
                  :rating_ids.sync="edit_aspect.rating_ids"
                />
              </v-card-text>

              <!-- V-card acties -->
              <v-card-actions>
                <v-btn @click="close"> Cancel</v-btn>
                <v-btn color="primary" @click="updateForm"> Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </template>
        <!-- Items bewerken/verwijderen knoppen -->
        <template #[`item.actions`]="{ item }">
          <v-icon small class="mr-2" @click="editItem(item)">
            mdi-pencil
          </v-icon>
        </template>
      </v-data-table>
    </v-card-text>

    <v-card-actions>
      <!-- New Item Dialog -->
      <v-dialog
        @click:outside="close"
        v-model="new_aspect_dialog"
        max-width="800"
      >
        <!-- New Item Button -->
        <template #activator="{ on, attrs }">
          <v-btn color="primary" outlined v-bind="attrs" v-on="on">
            New Aspect
          </v-btn>
        </template>
        <!-- New Item Form -->
        <v-card>
          <v-card-title>
            <span class="text-h5">{{ formTitle }}</span>
          </v-card-title>
          <!-- V-card text -->
          <v-card-text>
            <!-- Form In AspectsForm File -->
            <AspectsForm
              :title.sync="edit_aspect.title"
              :short_description.sync="edit_aspect.short_description"
              :description.sync="edit_aspect.description"
              :external_url.sync="edit_aspect.external_url"
              :rating_ids.sync="edit_aspect.rating_ids"
            />
          </v-card-text>

          <!-- V-card acties -->
          <v-card-actions>
            <v-btn @click="close"> Cancel</v-btn>
            <v-btn color="primary" @click="submitForm"> Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  // data variables
  data: () => ({
    edit_aspect_dialog: false,
    new_aspect_dialog: false,
    headers: [
      {text: 'Titel', value: 'title'},
      {text: 'Korte Beschrijving', value: 'short_description'},
      {text: 'Beschrijving', value: 'description'},
      {text: 'Link', value: 'external_url'},
      {text: 'Ratings', value: 'ratings'},
      {text: 'Actions', value: 'actions', sortable: false},
    ],
    aspects: [],
    aspectsRatings: [],
    edit_aspect: {
      title: '',
      short_description: '',
      description: '',
      external_url: '',
      rating_ids: '',
      default_ratings: [],
    },
    editedIndex: -1,
  }),

  // changes title of dialog form to either New Aspect or Edit Aspect
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Aspect' : 'Edit Aspect'
    },
  },

  // watch dialog for changes
  watch: {
    dialog(val) {
      val || this.close()
    },
  },

  // async fetch for aspects and ratings
  async fetch() {
    this.aspects = await this.$axios.$get(`/aspects`)
  },

  // Methods/Functions
  methods: {
    // wich item is being edited, method/function
    editItem(item) {
      this.editedIndex = this.aspects.indexOf(item)
      this.edit_aspect = Object.assign({}, item)
      this.edit_aspect_dialog = true
      this.edit_aspect.default_ratings = item.ratings
    },

    // closes dialog and resets parameters, method/function
    close() {
      this.edit_aspect_dialog = false
      this.new_aspect_dialog = false
      this.edit_aspect = {
        title: '',
        short_description: '',
        description: '',
        external_url: '',
        rating_ids: '',
        default_ratings: [],
      }
      this.$nextTick(() => {
        this.editedIndex = -1
      })
    },

    // Post method/function
    async submitForm() {
      this.aspects.push(await this.$axios.$post('/aspects', this.edit_aspect))
      this.close()
    },

    // patch/update method/function
    async updateForm() {
      const editet_aspect = await this.$axios.$patch(
        `/aspects/${this.aspects[this.editedIndex].id}`,
        this.edit_aspect
      )
      this.aspects.splice(this.editedIndex, 1, editet_aspect)
      this.close()
    },
  },
}
</script>
