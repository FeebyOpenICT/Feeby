<template>
  <div id="header">
    <v-card
      v-for="card in lists"
      :key="card.id"
      class="postcard"
    >
      <div class="header">
        <v-card-title>{{ card.title }}</v-card-title>
        <v-card-subtitle>{{ card.date }} - {{ card.id }}</v-card-subtitle>
      </div>
      <v-card-text id="body">
        {{ card.text }}
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'CardCom',
  data () {
    return {
      lists: [
        {
          id: 1,
          title: 'test1',
          date: '11-03-2022',
          text: 'test text 1'
        },
        {
          id: 3,
          title: 'test3',
          date: '07-02-2022',
          text: 'test text 3'
        },
        {
          id: 2,
          title: 'test2',
          date: '14-03-2022',
          text: 'test text 2'
        },
        {
          id: 5,
          title: 'test5',
          date: '15-05-2022',
          text: 'test text 5'
        },
        {
          id: 6,
          title: 'test6',
          date: '07-06-2022',
          text: 'test text 6'
        },
        {
          id: 4,
          title: 'test4',
          date: '14-04-2022',
          text: 'test text 4'
        }
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
