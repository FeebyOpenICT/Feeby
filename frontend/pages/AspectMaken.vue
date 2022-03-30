<template>
  <div>
    <HeaderCom />
    <AspectAanmaken />
    <FooterCom />
  </div>
</template>

<script>
import FooterCom from '~/components/FooterCom.vue'
import AspectAanmaken from '~/components/AspectCards/AspectAanmaken'
import HeaderCom from '~/components/HeaderCom.vue'
export default {
  name: 'AspectMaken',
  components: { AspectAanmaken, HeaderCom, FooterCom }
}
</script>
