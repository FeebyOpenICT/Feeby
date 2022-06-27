<template>
  <v-btn outlined color="primary" @click="log">Feedback aanvragen</v-btn>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "RequestFeedback",
  props: {
    revisionId: Number
  },
  methods: {
    log() {
      console.log(this.revisionId)
    }
  }
})
</script>

<style scoped>

</style>
