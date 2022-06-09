<template>
  <div>
    <h1 class="mx-auto">Admin Pagina</h1>
    <v-divider />
    <v-row>
      <v-col> </v-col>
      <v-col> <AspectsInzien /> </v-col>
    </v-row>
  </div>
</template>

<script>
import AspectsInzien from '~/components/AspectsInzien.vue'
export default {
  name: 'aspects-ratings',
  middleware: ['authenticated'],
  components: { AspectsInzien },
}
</script>
