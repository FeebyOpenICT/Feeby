<template>
  <div>
    <div
      v-for="card in lists"
      id="header"
      :key="card.id"
      :sort-by="sortBy"
      :sort-desc="sortDesc"
    >
      <v-card class="postcard">
        <div class="header">
          <v-card-title>{{ card.title }}</v-card-title>
          <v-card-subtitle>{{ card.date }}</v-card-subtitle>
        </div>
        <v-card-text id="body">
          {{ card.text }}
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
      sortDesc: false,
      sortBy: 'id',
      lists: [
        { id: 1, title: 'test1', date: '11-03-2022', text: 'test text 1' },
        { id: 3, title: 'test3', date: '07-02-2022', text: 'test text 3' },
        { id: 2, title: 'test2', date: '14-03-2022', text: 'test text 2' }
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
