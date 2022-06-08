<template>
  <!-- Data Tabel -->
  <v-data-table
    :headers="headers"
    :items="ratings"
    sort-by="title"
    class="elevation-1 ma-3 rounded-lg"
    data-app
  >
    <!-- De Header van het Tabel -->
    <template #top>
      <v-toolbar flat>
        <v-toolbar-title>Mijn Ratings</v-toolbar-title>
        <v-divider class="mx-4" inset vertical />
        <v-spacer />

        <!-- New Item Dialog -->
        <v-dialog v-model="dialogNew" max-width="70%">
          <!-- New Item Button -->
          <template #activator="{ on, attrs }">
            <v-btn
              color="primary"
              fab
              small
              fixed
              top
              right
              v-bind="attrs"
              v-on="on"
            >
              <v-icon> mdi-plus </v-icon>
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="ratingsNew.title"
                      counter
                      maxlength="255"
                      label="Rating Title"
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="ratingsNew.short_description"
                      counter
                      maxlength="255"
                      label="Korte Beschrijving"
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-textarea
                      v-model="ratingsNew.description"
                      counter
                      maxlength="1000"
                      label="Beschrijving"
                    />
                  </v-col>
                </v-row>
              </v-container>
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

        <!-- Edit Item Dialog -->
        <v-dialog v-model="dialog" max-width="70%">
          <!-- V-card Form -->
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="ratingsNew.title"
                      counter
                      maxlength="255"
                      label="Rating Title"
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="ratingsNew.short_description"
                      counter
                      maxlength="255"
                      label="Korte Beschrijving"
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-textarea
                      v-model="ratingsNew.description"
                      counter
                      maxlength="1000"
                      label="Beschrijving"
                    />
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <!-- V-card acties -->
            <v-card-actions>
              <v-btn class="mx-auto" color="blue darken-1" text @click="close">
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
      </v-toolbar>
    </template>
    <!-- Items bewerken/verwijderen knoppen -->
    <template #[`item.actions`]="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
    </template>
  </v-data-table>
</template>

<script>
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
    ratingsNew: {
      title: '',
      short_description: '',
      description: '',
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
      this.ratings.push(await this.$axios.$post('/ratings', this.ratingsNew))
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
}
</script>
