<template>
  <div>
    <div
      v-for="list in lists"
      id="header"
      :key="list.id"
    >
      <v-card class="postcard">
        <div class="header">
          <v-card-title>{{ list.title }}</v-card-title>
          <v-card-subtitle>{{ list.date }}</v-card-subtitle>
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
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardCom',
  data () {
    return {
      lists: [
        { id: 1, title: 'test1', date: '11-03-2022' },
        { id: 2, title: 'test2', date: '14-03-2022' },
        { id: 3, title: 'test3', date: '17-02-2022' }
      ]
    }
  }
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
      margin-bottom: 2vw;
  }
  .header{
      background-color: #0079CF;
      color: white;
  }
</style>
