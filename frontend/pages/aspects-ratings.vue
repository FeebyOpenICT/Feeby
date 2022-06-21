<template>
  <v-row>
    <v-col> <AspectsRatingsInzien /> </v-col>
    <v-col> </v-col>
  </v-row>
</template>

<script>
import AspectsRatingsInzien from '~/components/RatingsTableCard.vue'
export default {
  name: 'aspects-ratings',
  middleware: ['authenticated', 'authorization'],
  meta: {
    roles: ['admin'],
  },
  components: { AspectsRatingsInzien },
}
</script>
