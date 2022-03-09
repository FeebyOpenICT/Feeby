<template>
  <v-list
    nav
    dense
  >
    <v-list-item-title>
      Menu
    </v-list-item-title>
    <v-list-item>
      Profiel
    </v-list-item>
    <v-list-item>
      Toegang Beheer
    </v-list-item>
  </v-list>
</template>
<script>
export default {
  name: 'ModalCom'
}
</script>
<style scoped>
.modalmenu{
  height: 100%;
  width: 25%;
  overflow: hidden;
  z-index: 10;
}
</style>
