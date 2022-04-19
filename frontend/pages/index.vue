<template>
  <div id="page-container">
    <div id="content-wrap">
      <HeaderCom />
      <addButton />
      <CardCom />
    </div>
    <footer id="footer" />
  </div>
</template>

<script>
import CardCom from '~/components/CardCom.vue'
import HeaderCom from '~/components/HeaderCom.vue'
import '~/.css/styles.css'
export default {
  name: 'IndexPage',
  components: { CardCom, HeaderCom }
}
</script>
