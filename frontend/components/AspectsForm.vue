<template>
  <v-container>
    <v-row>
      <v-text-field
        :value="title"
        @input="$emit('update:title', $event)"
        counter
        maxlength="255"
        label="Aspect Title"
        outlined
      />
    </v-row>
    <v-row>
      <v-textarea
        :value="short_description"
        @input="$emit('update:short_description', $event)"
        counter
        maxlength="255"
        label="Korte Beschrijving"
        outlined
      />
    </v-row>
    <v-row>
      <v-textarea
        :value="description"
        @input="$emit('update:description', $event)"
        counter
        maxlength="1000"
        label="Beschrijving"
        outlined
      />
    </v-row>
    <v-row>
      <v-text-field
        :value="external_url"
        @input="$emit('update:external_url', $event)"
        counter
        maxlength="2000"
        label="Link"
        outlined
      />
    </v-row>
    <v-row>
      <v-select
        :value="rating_ids"
        @input="$emit('update:rating_ids', $event)"
        :items="aspectsRatings"
        label="Rating"
        multiple
        counter
        item-text="title"
        item-value="id"
        chips
        outlined
      />
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'AspectsForm',
  props: {
    title: { type: String, required: true },
    short_description: { type: String, required: true },
    description: { type: String, required: true },
    external_url: { type: String, required: true },
    rating_ids: { type: [String, Array], required: true },
  },
  data() {
    return {
      aspectsRatings: [],
    }
  },
  emits: [
    'update:title',
    'update:short_description',
    'update:description',
    'update:external_url',
    'update:rating_ids',
  ],
  fetchOnServer: true,
  async fetch() {
    this.aspectsRatings = await this.$axios.$get(`/ratings`)
  },
}
</script>
