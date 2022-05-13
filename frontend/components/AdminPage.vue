<template class="container">
  <v-app>
    <HeaderCom />
    <div class="cardContainer">
      <v-Card
        class="mx-auto"
        height="350"
        width="700"
        outlined
      >
        <v-list-item-title
          class="text-h5 mb-1"
          style="background-color: #0079CF"
        >
          <h2 style="padding: 15px; color: white">Legoshi is best boi</h2>

        </v-list-item-title>
      </v-Card>
    </div>
  </v-app>
</template>

<script>
import HeaderCom from './HeaderCom.vue'
export default {
  components: { HeaderCom },
  name: 'AdminComponent',
  data () {
    return {
      AspectList: {
        title: '',
        description: ''
      }
    }
  }
}
</script>
