<template>
  <v-card>
    <v-card-title class="ml-2 pr-2">
      {{ post.title }}
      <v-spacer></v-spacer>
      <v-btn @click.prevent="() => {}" icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-card-title>
    <v-card-subtitle class="ml-2 pr-2">
      <table>
        <tr>
          <td class="pr-2">Ingeleverd op</td>
          <td>{{ formattedCreationTime }}</td>
        </tr>
        <tr>
          <td class="pr-2">Gemaakt door</td>
          <td>{{ post.user.fullname }}</td>
        </tr>
        <tr>
          <td class="pr-2">Email</td>
          <td>{{ post.user.canvas_email }}</td>
        </tr>
      </table>
    </v-card-subtitle>

    <!--    description and user-->
    <v-card-text>
      <p class="ml-2 pr-2">
        {{ post.description }}
      </p>
      <v-divider></v-divider>
    </v-card-text>

    <!--    Nulmeting-->
    <v-expansion-panels flat class="pa-0 my-n4 ml-2 pr-2">
      <v-expansion-panel>
        <v-expansion-panel-header class="text-h6">Nulmeting</v-expansion-panel-header>
        <v-expansion-panel-content>
          <feedback-data-table :feedback="nulmeting"/>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>

    <v-card-text>
      <v-divider></v-divider>
      <br/>
      <!--    Revisions and feedback-->
      <v-timeline dense>
        <revision
          v-for="(revision, index) in post.revisions"
          :revision="revision"
          :title="`Revisie ${index + 1}`"
          :feedback="filterOutNulmeting(revision.feedback)"
          :index="index"
        />
      </v-timeline>
    </v-card-text>

  </v-card>
</template>

<script lang="ts">
import Vue from "vue";
import {Feedback, GetPostByID} from "~/types/GetPostByID";
import {DateTime} from "luxon";

export default Vue.extend({
  name: "BeroepsProduct",
  data() {
    return {
      post: {} as GetPostByID,
      formattedCreationTime: "" as string
    }
  },
  async asyncData({params, $axios}) {
    const post = await $axios.$get<GetPostByID>(`/posts/${params.postid}`)
    const formattedCreationTime = DateTime.fromISO(post.time_created).toLocaleString({
      day: 'numeric',
      month: 'long',
      year: 'numeric'
    })
    return {
      post,
      formattedCreationTime
    }
  },
  methods: {
    filterOutNulmeting(feedback: Feedback[]): Feedback[] {
      return feedback.filter(f => f.reviewer.id !== this.post.user_id)
    },
  },
  computed: {
    nulmeting(): Feedback[] {
      return this.post.revisions[0].feedback.filter((f: Feedback) => f.reviewer.id === this.post.user_id)
    },
  },
})
</script>

<style scoped>
</style>
