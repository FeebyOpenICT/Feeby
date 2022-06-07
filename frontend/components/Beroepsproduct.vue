<template>
  <v-card>
    <v-app-bar color="white" elevation="0">
      <v-toolbar-title> {{ title }} </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
    <v-card-text>{{ description }}</v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'BeroepsProduct',
  props: {
    title: String,
    description: String,
  },
}
</script>
