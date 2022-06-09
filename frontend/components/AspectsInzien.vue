<template>
  <v-card>
    <v-card-title>Aspects</v-card-title>
    <v-card-text>
      <!-- Data Tabel -->
      <v-data-table :headers="headers" :items="aspects" sort-by="title">
        <!-- Rating Array To String Method -->
        <template #[`item.ratings`]="{ item }">
          <td>{{ getRatingNames(item.ratings) }}</td>
        </template>

        <template #top>
          <!-- Edit Item Dialog -->
          <v-dialog
            @click:outside="close"
            v-model="edit_aspect_dialog"
            max-width="800"
          >
            <!-- V-card Form -->
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
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
                <v-btn @click="close"> Cancel </v-btn>
                <v-btn color="primary" @click="submitForm"> Save </v-btn>
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
            <v-btn @click="close"> Cancel </v-btn>
            <v-btn color="primary" @click="submitForm"> Save </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    edit_aspect_dialog: false,
    new_aspect_dialog: false,
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
    edit_aspect: {
      title: '',
      short_description: '',
      description: '',
      external_url: '',
      rating_ids: '',
    },
    editedIndex: -1,
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Aspect' : 'Edit Aspect'
    },
  },

  watch: {
    dialog(val) {
      val || this.close()
    },
    // 'edit_aspect.ratings'(ratings) {
    //   return ratings.map((ratings_ids) => ratings_ids.id)
    // },
  },
  fetchOnServer: true,
  async fetch() {
    this.aspects = await this.$axios.$get(`/aspects`)
    this.aspectsRatings = await this.$axios.$get(`/ratings`)
  },
  methods: {
    editItem(item) {
      this.editedIndex = this.aspects.indexOf(item)
      this.edit_aspect = Object.assign({}, item)
      this.edit_aspect_dialog = true
    },

    close() {
      this.edit_aspect_dialog = false
      this.new_aspect_dialog = false
      this.edit_aspect = {
        title: '',
        short_description: '',
        description: '',
        external_url: '',
        rating_ids: '',
      }
      this.$nextTick(() => {
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
      this.aspects.push(await this.$axios.$post('/aspects', this.edit_aspect))
      this.close()
    },

    async updateForm() {
      if (this.editedIndex > -1) {
        await this.$axios.$patch(
          `/aspects/${this.ratings[this.editedIndex].id}`,
          this.edit_aspect
        )
        Object.assign(this.aspects[this.editedIndex], this.edit_aspect)
      } else {
        this.aspects.push(this.edit_aspect)
      }
      this.close()
    },
  },
}
</script>
