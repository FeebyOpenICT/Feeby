<template>
  <v-card>
    <v-app-bar color="white" elevation="0">
      <v-toolbar-title> Test beroepsproduct </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
    <v-card-text>dit is de bescrijving</v-card-text>
  </v-card>
</template>

<script>
export default {
  setup() {},
  props: {
    title: String,
    description: String,
  },
}
</script>
