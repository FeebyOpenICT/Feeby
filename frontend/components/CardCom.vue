<template>
  <div id="header">
    <v-card
      v-for="card in orderedLists"
      :key="card.id"
      class="postcard"
    >
      <div class="header">
        <v-card-title>{{ card.title }}</v-card-title>
        <v-card-subtitle>{{ card.date }}</v-card-subtitle>
      </div>
      <v-card-text id="body">
        {{ card.text }}
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'CardCom',
  data () {
    return {
      lists: [
        {
          id: 1,
          title: 'test1',
          date: '11-03-2022',
          text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.'
        },
        {
          id: 3,
          title: 'test3',
          date: '07-02-2022',
          text: 'tLorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.'
        },
        {
          id: 2,
          title: 'test2',
          date: '14-03-2022',
          text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.'
        },
        {
          id: 5,
          title: 'test5',
          date: '15-05-2022',
          text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.'
        },
        {
          id: 6,
          title: 'test6',
          date: '07-06-2022',
          text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.'
        },
        {
          id: 4,
          title: 'test4',
          date: '14-04-2022',
          text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.'
        }
      ]
    }
  },
  computed: {
    orderedLists () {
      return _.orderBy(this.lists, 'date')
    }
  }
}
</script>

<style scoped>
  .postcard{
      width: 90vw;
      height: 25vh;
      overflow: auto;
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
