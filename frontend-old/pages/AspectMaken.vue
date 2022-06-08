<template>
  <div>
    <HeaderCom />
    <AspectAanmaken />
  </div>
</template>

<script>
import AspectAanmaken from '~/components/AspectCards/AspectAanmaken'
import HeaderCom from '~/components/HeaderCom.vue'
export default {
  name: 'AspectMaken',
  components: { AspectAanmaken, HeaderCom }
}
</script>
