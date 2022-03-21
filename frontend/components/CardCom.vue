<template>
  <div id="header">
    <v-card
      v-for="card in orderedLists"
      :key="card.id"
      class="postcard"
    >
      <div class="cardheader">
        <v-card-title>{{ card.title }}</v-card-title>
        <v-card-subtitle>{{ card.time_created }}</v-card-subtitle>
      </div>
      <v-card-text id="body">
        {{ card.description }}
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import _ from 'lodash'
import '../style/style.css'

export default {
  name: 'CardCom',
  data () {
    return {
      lists: [
        {
          id: 1,
          user_id: 1,
          title: 'test1',
          description: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.',
          time_created: '11-03-2022',
          time_updated: ''
        },
        {
          id: 3,
          user_id: 1,
          title: 'test3',
          description: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.',
          time_created: '07-02-2022',
          time_updated: ''
        },
        {
          id: 2,
          user_id: 1,
          title: 'test2',
          description: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.',
          time_created: '14-03-2022',
          time_updated: ''
        },
        {
          id: 5,
          user_id: 1,
          title: 'test5',
          description: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.',
          time_created: '15-05-2022',
          time_updated: ''
        },
        {
          id: 6,
          user_id: 1,
          title: 'test6',
          description: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.',
          time_created: '07-06-2022',
          time_updated: ''
        },
        {
          id: 4,
          user_id: 1,
          title: 'test4',
          description: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.',
          time_created: '14-04-2022',
          time_updated: ''
        }
      ]
    }
  },
  computed: {
    orderedLists () {
      return _.orderBy(this.lists, 'time_created')
    }
  }
}
</script>

<style scoped>
.postcard{
    width: 90vw;
    height: 25vh;
    overflow: hidden;
    position: relative;
    left: 5vw;
    border-style: hidden solid solid;
    border-width: 1px;
    border-color: black;
    margin-bottom: 2vw;
    margin-top: 2vw;
  }

.cardheader{
    background-color: var(--blue);
    color: white;
}
</style>
