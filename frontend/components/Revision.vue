<template>
  <v-timeline-item
    fill-dot
    class="white--text mb-12"
    small
  >
    <template v-slot:icon>
      <span>{{ index + 1 }}</span>
    </template>
    <v-card flat>
      <v-card-title>{{ title }}</v-card-title>
      <v-card-subtitle>{{ formattedCreationTime }}</v-card-subtitle>
      <v-card-text>
        {{ revision.description }}
      </v-card-text>
      <feedback-data-table :feedback="feedback"/>
      <v-card-actions>
        <request-feedback :revision-id="revision.id"></request-feedback>
      </v-card-actions>
    </v-card>
  </v-timeline-item>
</template>

<script lang="ts">
import Vue, {PropType} from "vue";
import {Feedback, Revision} from "~/types/GetPostByID";
import {DateTime} from "luxon";

export default Vue.extend({
  name: "Revision",
  props: {
    revision: {
      type: Object as PropType<Revision>,
      required: true
    },
    title: String,
    index: Number,
    feedback: {
      type: Array as PropType<Feedback[]>,
      required: true
    }
  },
  computed: {
    formattedCreationTime() {
      return DateTime.fromISO(this.revision.time_created).toLocaleString({
        month: 'long',
        day: 'numeric',
        year: 'numeric'
      })
    }
  }
})
</script>

<style scoped>

</style>
