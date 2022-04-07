<template>
  <div>
    <HeaderCom />
    <AspectRatingInzien />
    <FooterCom />
  </div>
</template>

<script>
import HeaderCom from './HeaderCom.vue'
import FooterCom from './FooterCom.vue'
import AspectRatingInzien from './AspectCards/AspectRatingInzien.vue'
export default {
  name: 'HomePage',
  components: { HeaderCom, FooterCom, AspectRatingInzien }
}
</script>

<style scoped>
.testpage{
  height: 100vw;
  z-index: 1;
}
</style>
