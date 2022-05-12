<template class="container">
  <v-app>
    <HeaderCom />
    <div class="cardContainer">
      <v-Card
        height="350"
        width="350"
        outlined
      >
        <v-list-item-title
          v-model="AspectList.title"
        >

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
  },

}
</script>
