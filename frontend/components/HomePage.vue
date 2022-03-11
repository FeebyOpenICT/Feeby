<template>
  <div>
    <HeaderCom />
    <div class="testpage">
      <h3>FEEBY</h3>
      <p>hello</p>
      <CardCom />
    </div>
    <FooterCom />
  </div>
</template>

<script>
import HeaderCom from './HeaderCom.vue'
import FooterCom from './FooterCom.vue'
import CardCom from './CardCom.vue'

export default {
  name: 'HomePage',
  components: { HeaderCom, FooterCom, CardCom }
}
</script>

<style scoped>
.testpage{
  height: 100vw;
}
</style>
