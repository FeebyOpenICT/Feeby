<template>
  <!-- Data Tabel -->
  <v-data-table
    :headers="headers"
    :items="aspects"
    sort-by="title"
    class="elevation-1 ma-3 rounded-lg"
  >
    <template #[`item.ratings`]="{ item }">
      <td>{{ getRatingNames(item.ratings) }}</td>
    </template>

    <!-- De Header van het Tabel -->
    <template #top>
      <v-toolbar flat>
        <v-toolbar-title>Mijn Aspects</v-toolbar-title>
        <v-divider class="mx-4" inset vertical />
        <v-spacer />

        <!-- New Item Dialog -->
        <v-dialog v-model="dialogNew" max-width="70%" max-height="80%">
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
                      v-model="aspectsNew.title"
                      counter
                      maxlength="255"
                      label="Rating Title"
                      outlined
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-textarea
                      v-model="aspectsNew.short_description"
                      counter
                      maxlength="255"
                      label="Korte Beschrijving"
                      outlined
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-textarea
                      v-model="aspectsNew.description"
                      counter
                      maxlength="1000"
                      label="Beschrijving"
                      outlined
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-text-field
                      v-model="aspectsNew.external_url"
                      counter
                      maxlength="2000"
                      label="Link"
                      outlined
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-select
                      v-model="aspectsNew.rating_ids"
                      :items="aspectsRatings"
                      label="Rating"
                      multiple
                      counter
                      item-text="title"
                      item-value="id"
                      chips
                      outlined
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
        <v-dialog v-model="dialog" max-width="70%" max-height="80%">
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
                      v-model="aspectsNew.title"
                      counter
                      maxlength="255"
                      label="Rating Title"
                      outlined
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-textarea
                      v-model="aspectsNew.short_description"
                      counter
                      maxlength="255"
                      label="Korte Beschrijving"
                      outlined
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-textarea
                      v-model="aspectsNew.description"
                      counter
                      maxlength="1000"
                      label="Beschrijving"
                      outlined
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-text-field
                      v-model="aspectsNew.external_url"
                      counter
                      maxlength="2000"
                      label="Link"
                      outlined
                    />
                  </v-col>
                  <v-col cols="12" sm="6" md="6">
                    <v-select
                      v-model="aspectsNew.ratings"
                      :items="aspectsRatings"
                      label="Rating"
                      multiple
                      counter
                      item-text="title"
                      item-value="id"
                      chips
                      outlined
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
      { text: 'Link', value: 'external_url' },
      { text: 'Rating', value: 'ratings' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],
    aspects: [],
    aspectsRatings: [],
    aspectsNew: {
      title: '',
      short_description: '',
      description: '',
      external_url: '',
      rating_ids: '',
    },
    editedIndex: -1,
    defaultItem: {
      title: '',
      short_description: '',
      description: '',
      external_url: '',
      rating_ids: '',
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
    'aspectsNew.ratings'(ratings) {
      return ratings.map((ratings_ids) => ratings_ids.id)
    },
  },
  fetchOnServer: true,
  async fetch() {
    this.aspects = await this.$axios.$get(`/aspects`)
    this.aspectsRatings = await this.$axios.$get(`/ratings`)
  },
  methods: {
    editItem(item) {
      this.editedIndex = this.aspects.indexOf(item)
      this.aspectsNew = Object.assign({}, item)
      this.dialog = true
    },

    close() {
      this.dialog = false
      this.dialogNew = false
      this.$nextTick(() => {
        this.aspectsNew = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    getRatingNames: (ratings) => {
      return ratings
        .map((rating) => rating.title)
        .join(', ')
        .toString()
    },

    async submitForm() {
      this.aspects.push(await this.$axios.$post('/aspects', this.aspectsNew))
      this.close()
    },

    async updateForm() {
      if (this.editedIndex > -1) {
        await this.$axios.$patch(
          `/aspects/${this.ratings[this.editedIndex].id}`,
          this.aspectsNew
        )
        Object.assign(this.aspects[this.editedIndex], this.aspectsNew)
      } else {
        this.aspects.push(this.aspectsNew)
      }
      this.close()
    },
  },
}
</script>
