<template>
  <div>
    <HeaderCom />
    <HomePage />
  </div>
</template>

<script>
import HomePage from '~/components/HomePage.vue'
import HeaderCom from '~/components/HeaderCom.vue'
export default {
  name: 'IndexPage',
  components: { HomePage, HeaderCom }
}
</script>
