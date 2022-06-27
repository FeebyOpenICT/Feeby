<template>
  <v-timeline-item fill-dot class="white--text mb-12" small>
    <!--    Icon-->
    <template v-slot:icon>
      <v-icon color="white">mdi-plus</v-icon>
    </template>

    <v-dialog v-model="dialog" max-width="800px" persistent>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Nieuwe Revisie Inleveren
        </v-btn>
      </template>
      <v-card ref="form">
        <v-card-title><span class="text-h5">Nieuwe Revisie</span></v-card-title>
        <v-card-text>
          <v-textarea
            ref="description"
            v-model="form.description"
            maxlength="1000"
            :rules="[rules.required, rules.counter]"
            counter
            label="Beschrijving"
            required
          >
          </v-textarea>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="submit"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!--    Snackbar popup -->
    <v-snackbar v-model="snackbar" bottom>
      {{ snackbar_text }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="primary"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-timeline-item>
</template>

<script lang="ts">
import Vue from "vue";
import {CreateRevision} from "~/types/CreateRevision";

export default Vue.extend({
  name: "CreateRevisionButton",
  data() {
    return {
      rules: {
        required: (value: any) => !!value || 'Required.',
        counter: (value: string | any[]) => value.length <= 1000 || 'Max 1000 characters',
      },
      formHasErrors: false,
      dialog: false,
      snackbar: false,
      snackbar_text: "",
      form: {
        description: ""
      }
    }
  },
  props: {
    postId: Number
  },
  methods: {

    async submit() {
      this.dialog = false
      try {
        const revision = await this.$axios.$post<CreateRevision>(`/posts/${this.postId}/revisions`, this.form)
        this.$emit('revision-created', revision)
        this.form = {
          description: ""
        }
        this.snackbar_text = "Nieuwe revisie succesvol ingeleverd"
        this.snackbar = true
      } catch {
        this.snackbar_text = "Er is helaas iets fout gegaan met de revisie inleveren, probeer het opnieuw"
        this.snackbar = true
      }
    }
  }
})
</script>

<style scoped>

</style>
