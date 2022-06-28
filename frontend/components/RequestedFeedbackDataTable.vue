<template>
  <v-card flat>
    <v-card-title>Feedback status</v-card-title>
    <v-data-table :headers="headers" :items="items" :items-per-page="5">
      <template v-slot:item.status="{ item }">
        {{ calculateStatus(item) }}
      </template>
    </v-data-table>
  </v-card>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'
import { GetInvitesOnRevision, Invite } from '~/types/GetInvitesOnRevision'
export default Vue.extend({
  name: 'RequestedFeedbackDataTable',
  data() {
    return {
      headers: [
        { text: 'Gebruiker', value: 'user.fullname' },
        { text: 'Status', value: 'status' },
      ],
    }
  },
  props: {
    items: {
      type: Array as PropType<GetInvitesOnRevision>,
    },
  },
  methods: {
    calculateStatus(invite: Invite) {
      if (invite.time_finished) return 'Klaar'
      if (invite.time_opened) return 'Begonnen'
      return 'Aangevraagd'
    },
  },
})
</script>

<style scoped></style>
