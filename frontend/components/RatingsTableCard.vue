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
          <v-dialog v-model="dialog" max-width="70%">
            <!-- V-card Form -->
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
<!--                <AspectsRatingsField-->
<!--                  v-model:title="ratingsNew.title"-->
<!--                  v-model:short_description="ratingsNew.short_description"-->
<!--                  v-model:description="ratingsNew.description"-->
<!--                />-->
              </v-card-text>

              <!-- V-card acties -->
              <v-card-actions>
                <v-btn
                  class="mx-auto"
                  color="blue darken-1"
                  text
                  @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                  class="mx-auto"
                  color="blue darken-1"
                  text
                  @click="updateForm"
                >
                  Save
                </v-btn>
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
      <v-dialog v-model="dialogNew" max-width="70%">
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
              :title.sync="new_rating.title"
              :short_description.sync="new_rating.short_description"
              :description.sync="new_rating.description"
            />
          </v-card-text>
          <v-card-actions>
            <v-btn class="mx-auto" color="blue darken-1" text @click="close">
              Cancel
            </v-btn>
            <v-btn
              class="mx-auto"
              color="blue darken-1"
              text
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
    dialog: false,
    dialogNew: false,
    dialogDelete: false,
    headers: [
      { text: 'Titel', value: 'title' },
      { text: 'Korte Beschrijving', value: 'short_description' },
      { text: 'Beschrijving', value: 'description' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],
    ratings: [],
    new_rating: {
      title: '',
      description: '',
      short_description: ''
    },
    editedIndex: -1,
    defaultItem: {
      title: '',
      short_description: '',
      description: '',
    },
  }),
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
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
      this.ratingsNew = Object.assign({}, item)
      this.dialog = true
    },
    close() {
      this.dialog = false
      this.dialogNew = false
      this.$nextTick(() => {
        this.ratingsNew = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    async submitForm() {
      this.ratings.push(await this.$axios.$post('/ratings', this.new_rating))
      this.close()
    },
    async updateForm() {
      if (this.editedIndex > -1) {
        await this.$axios.$patch(
          `/ratings/${this.ratings[this.editedIndex].id}`,
          this.ratingsNew
        )
        Object.assign(this.ratings[this.editedIndex], this.ratingsNew)
      } else {
        this.ratings.push(this.ratingsNew)
      }
      this.close()
    },
  },
  components: { AspectsRatingsField },
}
</script>
