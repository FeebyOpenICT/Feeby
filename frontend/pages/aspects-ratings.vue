<template>
  <div>
    <h1 class="mx-auto">Admin Pagina</h1>
    <v-divider />
    <v-row>
      <v-col> <AspectsRatingsInzien /> </v-col>
      <v-col> </v-col>
    </v-row>
  </div>
</template>

<script>
import AspectsRatingsInzien from '~/components/AspectsRatingsInzien.vue'
export default {
  name: 'aspects-ratings',
  middleware: ['authenticated'],
  components: { AspectsRatingsInzien },
}
</script>
