<template>
  <div>
    <HeaderCom />
    <AspectInzien />
  </div>
</template>

<script>
import AspectInzien from '~/components/AspectCards/AspectInzien'
import HeaderCom from '~/components/HeaderCom.vue'
export default {
  name: 'AdminPagina',
  components: { AspectInzien, HeaderCom }
}
</script>
