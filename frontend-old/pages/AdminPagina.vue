<template>
  <div>
    <HeaderCom />
    <AspectRatingInzien />
  </div>
</template>

<script>
import AspectRatingInzien from '~/components/AspectCards/AspectRatingInzien.vue'
import HeaderCom from '~/components/HeaderCom.vue'
export default {
  name: 'AdminPagina',
  components: { AspectRatingInzien, HeaderCom }
}
</script>
