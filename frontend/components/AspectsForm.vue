<template>
  <!-- Aspects Form Container -->
  <v-container>
    <v-row>
      <!-- Title Field -->
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
      <!-- Short Description Textarea -->
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
      <!-- Description Textarea -->
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
      <!-- External_url Field -->
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
      <!-- Rating_ids Select -->
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
  // Name Of Template
  name: 'AspectsForm',

  // Property With The Type Of Property
  props: {
    title: { type: String, required: true },
    short_description: { type: String, required: true },
    description: { type: String, required: true },
    external_url: { type: String, required: true },
    rating_ids: { type: String, Array, required: true },
  },

  // Data Variable
  data() {
    return {
      aspectsRatings: [],
    }
  },

  // Emits For Everything That Need To Be Emited To Another Component
  emits: [
    'update:title',
    'update:short_description',
    'update:description',
    'update:external_url',
    'update:rating_ids',
  ],

  fetchOnServer: true,

  // Async Fetch for Ratings
  async fetch() {
    this.aspectsRatings = await this.$axios.$get(`/ratings`)
  },
}
</script>
