<template>
  <div class="menu">
    <v-app-bar color="#0079CF">
      <v-app-bar-nav-icon class="navIcon" @click="modal = true" />
      <v-toolbar-title>FEEBY</v-toolbar-title>
    </v-app-bar>
    <v-navigation-drawer
      v-model="modal"
      absolute
      temporary
    >
      <ModalCom />
    </v-navigation-drawer>
  </div>
</template>
<script>
import ModalCom from './ModalCom.vue'
export default {
  name: 'HeaderCom',
  components: { ModalCom },
  data: () => ({
    modal: false
  })
}
</script>
<style scoped>
.navIcon{
  position: absolute;
  right: 2%;
}
.menu {
    overflow: hidden;
    top: 0;
    position: sticky;
    z-index: 2;
  }
</style>
