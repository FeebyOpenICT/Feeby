<template>
  <v-card flat>
    <v-data-table
      hide-default-footer
      disable-pagination
      :headers="headers"
      :items="feedback"
      :items-per-page="-1"
    >
      <template v-slot:item.reviewer="{ item }">
        <AvatarAndName
          class="pa-n4"
          :canvas_email="item.reviewer.canvas_email"
          :fullname="item.reviewer.fullname"
        />
      </template>
    </v-data-table>
  </v-card>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'
import { Feedback } from '~/types/GetPostByID'

export default Vue.extend({
  name: 'FeedbackDataTable',
  props: {
    feedback: {
      type: Array as PropType<Feedback[]>,
      required: true,
    },
  },
  data() {
    return {
      headers: [
        {
          text: 'Reviewer',
          align: 'start',
          sortable: false,
          value: 'reviewer',
          width: '300px',
        },
        { text: 'Aspect', sortable: false, value: 'aspect.title' },
        { text: 'Rating', sortable: false, value: 'rating.title' },
        {
          text: 'Review',
          sortable: false,
          value: 'description',
          width: '50%',
        },
      ],
    }
  },
})
</script>

<style scoped></style>
