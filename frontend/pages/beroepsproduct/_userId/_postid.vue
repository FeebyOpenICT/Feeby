<template>
  <v-card>
    <v-card-title>{{ userId }} / {{ postId }}</v-card-title>
  </v-card>
</template>

<script>
export default {
  name: "_postId",
  data() {
    return {
    }
  },
  async asyncData({ params, $axios }) {
    const userId = params.userId
    const postId = params.postId
    const posts = await $axios.$get(`/users/${params.userId}/posts/${params.postid}`)
    console.log(posts)
    return { userId, postId, posts }
  }
}
</script>

<style scoped>

</style>
