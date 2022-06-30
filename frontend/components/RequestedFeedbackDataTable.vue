<template>
  <v-card flat>
    <v-data-table
      hide-default-footer
      :headers="headers"
      :items="items"
      disable-pagination
      :items-per-page="-1"
    >
      <template v-slot:item.status="{ item }">
        {{ item.time_opened ? 'Begonnen' : 'Aangevraagd' }}
      </template>
    </v-data-table>
  </v-card>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'
import { GetInvitesOnRevision } from '~/types/GetInvitesOnRevision'
export default Vue.extend({
  name: 'RequestedFeedbackDataTable',
  data() {
    return {
      headers: [
        { text: 'Naam', value: 'user.fullname' },
        { text: 'E-mail', value: 'user.canvas_email' },
        { text: 'Status', value: 'status' },
      ],
    }
  },
  props: {
    items: {
      type: Array as PropType<GetInvitesOnRevision>,
    },
  },
})
</script>

<style scoped></style>
