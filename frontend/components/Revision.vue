<template>
  <v-timeline-item fill-dot class="white--text mb-12" small>
    <template v-slot:icon>
      <span>{{ index + 1 }}</span>
    </template>
    <v-card flat>
      <v-card-title>{{ title }}</v-card-title>
      <v-card-subtitle>{{ formattedCreationTime }}</v-card-subtitle>
      <v-card-text>
        {{ revision.description }}
      </v-card-text>
      <feedback-data-table
        v-model:selectedUsers="selectedUsers"
        :feedback="feedback"
      />
      <v-card-actions>
        <request-feedback
          :alreadySelectedUsers="selectedUsers"
          :revision-id="revision.id"
          @invited="addInvites"
        ></request-feedback>
      </v-card-actions>
    </v-card>
  </v-timeline-item>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'
import { Feedback, Revision, User } from '~/types/GetPostByID'
import { DateTime } from 'luxon'
import { GetInvitesOnRevision } from '~/types/GetInvitesOnRevision'

export default Vue.extend({
  name: 'Revision',
  props: {
    revision: {
      type: Object as PropType<Revision>,
      required: true,
    },
    title: String,
    index: Number,
    feedback: {
      type: Array as PropType<Feedback[]>,
      required: true,
    },
  },
  data() {
    return {
      invites: [] as GetInvitesOnRevision,
    }
  },
  async fetch() {
    this.invites = await this.$axios.$get<GetInvitesOnRevision>(
      `/revisions/${this.revision.id}/invites`
    )
  },
  computed: {
    formattedCreationTime(): string {
      return DateTime.fromISO(this.revision.time_created).toLocaleString({
        month: 'long',
        day: 'numeric',
        year: 'numeric',
      })
    },
    selectedUsers(): User[] {
      return this.invites.map((invite) => invite.user)
    },
  },
  methods: {
    addInvites(invites: GetInvitesOnRevision) {
      this.invites = [...this.invites, ...invites]
    },
  },
})
</script>

<style scoped></style>
