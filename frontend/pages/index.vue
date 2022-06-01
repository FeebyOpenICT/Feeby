<template>
  <div>
    <beroepsproduct
      title="Test Beroepsproduct"
      description="Dit is een test beschrijving"
    />

    <v-btn
      color="primary"
      fab
      large
      dark
      fixed
      bottom
      right
      to="/beroepsproduct-inleveren"
    >
      <v-icon>mdi-plus</v-icon>
    </v-btn>
  </div>
</template>

<script>
import Beroepsproduct from '~/components/Beroepsproduct.vue'
export default {
  components: { Beroepsproduct },
  name: 'IndexPage',
}
</script>
