<template>
  <v-container>
    <v-row>
      <v-text-field
        @input="$emit('update:title', $event)"
        :value="title"
        counter
        maxlength="255"
        label="Rating Title"
      />
    </v-row>
    <v-row>
      <v-text-field
        @input="$emit('update:short_description', $event.target.value)"
        :value="short_description"
        counter
        maxlength="255"
        label="Korte Beschrijving"
      />
    </v-row>
    <v-row>
      <v-textarea
        @input="$emit('update:description', $event.target.value)"
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
    title: String,
    short_description: String,
    description: String,
  },
  emits: ['update:title', 'update:short_description', 'update:description'],
}
</script>
