<template>
  <v-hover v-slot="{ hover }">
    <v-card :elevation="hover ? 6 : undefined " :to="`/beroepsproduct/${post.id}`">
      <v-list-item two-line>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            {{ post.title }}
          </v-list-item-title>
          <v-list-item-subtitle>{{ formattedCreationTime }}</v-list-item-subtitle>
        </v-list-item-content>
        <v-list-item-action>
          <v-btn @click.prevent="() => {}" icon>
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
      <v-card-text>{{ post.description }}</v-card-text>
    </v-card>
  </v-hover>
</template>

<script lang="ts">
import Vue, {PropType} from "vue";
import {Post} from "~/types/GetPosts";
import {DateTime} from "luxon";

export default Vue.extend({
  name: 'PostCard',
  data() {
    return {
      hover: false
    }
  },
  props: {
    post: {
      type: Object as PropType<Post>,
      required: true
    }
  },
  computed: {
    formattedCreationTime() {
      return DateTime.fromISO(this.post.time_created).toLocaleString({month: 'long', day: 'numeric', year: 'numeric'})
    }
  }
})
</script>
