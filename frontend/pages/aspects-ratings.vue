<template>
  <v-row>
    <v-col> </v-col>
    <v-col> <AspectsInzien /> </v-col>
  </v-row>
</template>

<script>
import AspectsInzien from '~/components/AspectsInzien.vue'
export default {
  name: 'aspects-ratings',
  middleware: ['authenticated'],
  components: { AspectsInzien },
}
</script>
