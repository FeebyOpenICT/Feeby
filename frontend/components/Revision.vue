<template>
  <v-timeline-item fill-dot class="white--text mb-12" small>
    <template v-slot:icon>
      <span>{{ index + 1 }}</span>
    </template>
    <v-card flat outlined>
      <v-card-title
        ><span class="text-h4">{{ title }}</span></v-card-title
      >
      <v-card-subtitle>{{ formattedCreationTime }}</v-card-subtitle>
      <v-card-text>
        {{ revision.description }}
      </v-card-text>

      <!--      Given feedback -->

      <!--      Requested feedback from -->
      <v-expansion-panels flat hover multiple>
        <v-expansion-panel>
          <v-expansion-panel-header
            ><span class="text-button">feedback</span></v-expansion-panel-header
          >
          <v-expansion-panel-content>
            <feedback-data-table
              v-model:selectedUsers="selectedUsers"
              :feedback="feedback"
            />
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel v-if="filteredInvites.length > 0">
          <v-expansion-panel-header
            ><span class="text-button">status</span></v-expansion-panel-header
          >
          <v-expansion-panel-content>
            <requested-feedback-data-table
              :items="filteredInvites"
            ></requested-feedback-data-table>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

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
    filteredInvites(): GetInvitesOnRevision {
      return this.invites.filter((invite) => !invite.time_finished)
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
