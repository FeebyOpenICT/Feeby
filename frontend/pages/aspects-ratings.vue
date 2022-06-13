<template>
  <v-row>
    <v-col> </v-col>
    <v-col> <AspectsBeheren /> </v-col>
  </v-row>
</template>

<script>
import AspectsBeheren from '~/components/AspectsBeheren.vue'
export default {
  name: 'aspects-ratings',
  middleware: ['authenticated'],
  components: { AspectsBeheren },
}
</script>
