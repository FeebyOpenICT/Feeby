<template>
  <div>
    <HeaderCom />
    <addButton />
    <CardCom />
    <FooterCom />
  </div>
</template>

<script>
import FooterCom from '~/components/FooterCom.vue'
import CardCom from '~/components/CardCom.vue'
import HeaderCom from '~/components/HeaderCom.vue'
export default {
  name: 'IndexPage',
  components: { FooterCom, CardCom, HeaderCom }
}
</script>
