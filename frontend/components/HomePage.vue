<template>
  <div>
    <CardCom />
    <FooterCom />
  </div>
</template>

<script>
import FooterCom from './FooterCom.vue'
import CardCom from './CardCom.vue'

export default {
  name: 'HomePage',
  components: { FooterCom, CardCom }
}
</script>
