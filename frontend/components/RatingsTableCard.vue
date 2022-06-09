<template>
  <v-card>
    <v-card-title>Ratings</v-card-title>
    <v-card-text>
      <!-- Data Tabel -->
      <v-data-table
        :headers="headers"
        :items="ratings"
        sort-by="title"
        data-app
      >
        <!-- De Header van het Tabel -->
        <template #top>
          <!-- New Item Dialog -->

          <!-- Edit Item Dialog -->
          <v-dialog @click:outside="close" v-model="edit_rating_dialog" max-width="800">
            <!-- V-card Form -->
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <AspectsRatingsField
              :title.sync="edit_rating.title"
              :short_description.sync="edit_rating.short_description"
              :description.sync="edit_rating.description"
            />
              </v-card-text>

              <!-- V-card acties -->
              <v-card-actions>
                <v-btn @click="close">
                  Cancel
                </v-btn>
                <v-btn
                  color="primary"
                  @click="updateForm"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </template>
        <!-- Items bewerken knoppen -->
        <template #[`item.actions`]="{ item }">
          <v-icon small class="mr-2" @click="editItem(item)">
            mdi-pencil
          </v-icon>
        </template>
      </v-data-table>
    </v-card-text>
    <v-card-actions>
      <v-dialog @click:outside="close" v-model="new_rating_dialog" max-width="800">
        <!-- New Item Button -->
        <template #activator="{ on, attrs }">
          <v-btn color="primary" outlined v-bind="attrs" v-on="on">
            New Rating
          </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">{{ formTitle }}</span>
          </v-card-title>
          <v-card-text>
            <AspectsRatingsField
              :title.sync="edit_rating.title"
              :short_description.sync="edit_rating.short_description"
              :description.sync="edit_rating.description"
            />
          </v-card-text>
          <v-card-actions>
            <v-btn @click="close">
              Cancel
            </v-btn>
            <v-btn
              color="primary"
              @click="submitForm"
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card-actions>
  </v-card>
</template>

<script>
import AspectsRatingsField from './RatingsForm.vue'
export default {
  data: () => ({
    edit_rating_dialog: false,
    new_rating_dialog: false,
    headers: [
      { text: 'Titel', value: 'title' },
      { text: 'Korte Beschrijving', value: 'short_description' },
      { text: 'Beschrijving', value: 'description' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],
    ratings: [],
    edit_rating: {
      title: '',
      description: '',
      short_description: ''
    },
    editedIndex: -1
  }),
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Rating' : 'Edit Item'
    },
  },
  watch: {
    dialog(val) {
      val || this.close()
    },
  },
  fetchOnServer: true,
  async fetch() {
    this.ratings = await this.$axios.$get(`/ratings`)
  },
  methods: {
    editItem(item) {
      this.editedIndex = this.ratings.indexOf(item)
      this.edit_rating = Object.assign({}, item)
      this.edit_rating_dialog = true
    },
    close() {
      this.edit_rating_dialog = false
      this.new_rating_dialog = false
      this.edit_rating = {
        title: '',
        description: '',
        short_description: ''
      }
      this.$nextTick(() => {
        this.editedIndex = -1
      })
    },
    async submitForm() {
      this.ratings.push(await this.$axios.$post('/ratings', this.edit_rating))
      this.close()
    },
    async updateForm() {
      if (this.editedIndex > -1) {
        await this.$axios.$patch(
          `/ratings/${this.ratings[this.editedIndex].id}`,
          this.edit_rating
        )
        Object.assign(this.ratings[this.editedIndex], this.edit_rating)
      } else {
        this.ratings.push(this.edit_rating)
      }
      this.close()
    },
  },
  components: { AspectsRatingsField },
}
</script>
