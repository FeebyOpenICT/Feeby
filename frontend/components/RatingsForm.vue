<template>
  <v-container>
    <v-row>
      <v-text-field
        :value="title"
        @input="$emit('update:title', $event)"
        counter
        maxlength="255"
        label="Rating Title"
      />
    </v-row>
    <v-row>
      <v-text-field
        @input="$emit('update:short_description', $event)"
        :value="short_description"
        counter
        maxlength="255"
        label="Korte Beschrijving"
      />
    </v-row>
    <v-row>
      <v-textarea
        @input="$emit('update:description', $event)"
        :value="description"
        counter
        maxlength="1000"
        label="Beschrijving"
      />
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: 'AspectsRatingsField',
  props: {
    title: {type: String, required: true},
    short_description: {type: String, required: true},
    description: {type: String, required: true},
  },
  emits: ['update:title', 'update:short_description', 'update:description'],
}
</script>
