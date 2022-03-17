<template>
  <div>
    <HeaderCom />
    <PostTitle />
    <div class="testpage">
      <h1 class="pageTitle">Product inleveren</h1>
      <InputField />
      <UploadBox />
      <AspectCommunication />
      <AspectKnowledge/>

    </div>
    <FooterCom />
  </div>
</template>
<script>
import HeaderCom from './HeaderCom.vue'
import FooterCom from './FooterCom.vue'
export default {
  name: 'CreatePost',
  components: { HeaderCom, FooterCom }
}
</script>




<style scoped>
.testpage {
  height: 2000px;
  z-index: 1;
}
.testpage h1 {
  text-align: center;
}
</style>
