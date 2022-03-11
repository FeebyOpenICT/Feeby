<template>
  <v-card
    class="postcard"
  >
    <div id="header" class="header">
      <v-card-title>Post Card</v-card-title>
      <v-card-subtitle>11-03-2022</v-card-subtitle>
    </div>
    <v-card-text class="body">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
      Proin laoreet sapien at nibh luctus accumsan.
      Sed accumsan sem nulla, venenatis lacinia lacus pellentesque eget.
      Mauris vitae efficitur nisl.
      Ut mattis nisl ut rutrum commodo.
      Ut in tellus nunc.
      In venenatis, arcu ultrices condimentum vulputate, tortor purus ultrices tellus, eget congue nunc nunc in justo.
      Nulla at bibendum magna.
      Curabitur molestie a tortor non tempor.
      Nulla nunc justo, facilisis ut diam eu, condimentum ultricies augue.
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'CardCom'
}
</script>

<style scoped>
  .postcard{
      width: 90vw;
      height: 20vh;
      position: relative;
      left: 5vw;
      border-style: hidden solid solid;
      border-width: 1px;
      border-color: black;
  }
  .header{
      background-color: #0079CF;
      color: white;
  }
</style>
