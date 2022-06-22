<template>
  <v-row>
    <v-col> <AspectsBeheren /> </v-col>
    <v-col> <AspectsRatingsInzien /> </v-col>
  </v-row>
</template>

<script>
import AspectsBeheren from '~/components/AspectsBeheren.vue'
import AspectsRatingsInzien from '~/components/RatingsTableCard.vue'
export default {
  name: 'aspects-ratings',
  middleware: ['authenticated', 'authorization'],
  meta: {
    roles: ['admin'],
  },
  components: { AspectsRatingsInzien, AspectsBeheren },
}
</script>
