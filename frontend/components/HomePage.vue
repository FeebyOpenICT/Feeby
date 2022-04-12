<template>
  <div>
    <HeaderCom />
    <FooterCom />
  </div>
</template>

<script>
import HeaderCom from './HeaderCom.vue'
import FooterCom from './FooterCom.vue'
export default {
  name: 'HomePage',
  components: { HeaderCom, FooterCom }
}
</script>

<style scoped>
.testpage{
  height: 100vw;
  z-index: 1;
}
</style>
