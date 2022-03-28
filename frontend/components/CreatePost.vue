<template>
  <div>
    <HeaderCom />
    <PostTitle />
    <div class="postPage">
      <h1 class="pageTitle">Product inleveren</h1>
      <InputField />
      <UploadBox />
      <AspectCommunication />
      <AspectKnowledge/>

      <v-card
        v-for="post in posts"
        :key="post.id"
        class="cardsList"
      >
        <div class="postContainer">
        <v-card-title>{{post.title}}</v-card-title>
      </div>
      </v-card>
    </div>
    <FooterCom />
  </div>
</template>

<script>
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import { axiosInstance } from '../lib/axiosInstance'
import HeaderCom from './HeaderCom.vue'
import FooterCom from './FooterCom.vue'
export default {
  name: 'CreatePost',
  components: { HeaderCom, FooterCom },
  data () {
    return {
      posts: null
    }
  },
  mounted () {
    axiosInstance
      .get('api/v1/posts/self')
      .then(response => (this.posts = response.data))
      .catch(error => console.log(error))
  }
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
.cardsList{
  width: 90vw;
  max-width: 90vw;
  min-width: 30vw;
  height: 25vh;
  min-height: 10vw;
  max-height: 25vw;
  overflow: hidden;
  position: relative;
  left: 5vw;
  border-style: hidden solid solid;
  border-width: 1px;
  border-color: black;
  margin-bottom: 2vw;
  margin-top: 2vw;
}

</style>
