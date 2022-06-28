<template>
  <div>
    <v-dialog v-model="dialog" max-width="800px" persistent>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          outlined
          v-bind="attrs"
          v-on="on"
        >
          Feedback aanvragen
        </v-btn>
      </template>
      <v-card ref="form">
        <v-card-title><span class="text-h5">Feedback aanvragen</span></v-card-title>

        <!--        Search and select users-->
        <v-card-text>
          <v-autocomplete
            v-model="selectedUsers"
            :loading="loading"
            :items="foundFilteredUsers"
            :search-input.sync="search"
            auto-select-first
            multiple
            chips
            deletable-chips
            small-chips
            item-text="canvas_email"
            item-value="canvas_email"
            label="Studenten"
            placeholder="Begin met typen om door bestaande studenten te zoeken"
            prepend-icon="mdi-database-search"
            return-object
          >
            <template v-slot:selection="{item, attrs, selected, select}">
              <v-chip
                v-bind="attrs"
                :input-value="selected"
                close
                @click="select"
                @click:close="remove(item)"
              >
                <template>
                  {{ item.canvas_email }}
                </template>
              </v-chip>

            </template>
            <template v-slot:item="{ item, on, attrs }">
              <v-list-item v-on="on" v-bind="attrs" #default="{ active }">
                <v-list-item-action>
                  <v-checkbox :input-value="active"></v-checkbox>
                </v-list-item-action>
                <v-list-item-content>
                  <avatar-and-name :canvas_email="item.canvas_email" :fullname="item.fullname"/>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-autocomplete>
        </v-card-text>

        <!--        Actions-->
        <v-card-actions>
          <v-btn
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="primary"
            @click="submit"
          >
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

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
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import {SearchThroughUsers, User} from "~/types/SearchThroughUsers";
import {mapGetters} from "vuex";
import {InviteOnRevision} from "~/types/InviteOnRevision";

export default Vue.extend({
  name: "RequestFeedback",
  data() {
    return {
      snackbar_text: "" as string,
      snackbar: false as boolean,
      dialog: false as boolean,
      selectedUsers: [] as SearchThroughUsers,
      loading: false as boolean,
      foundUsers: [] as SearchThroughUsers,
      search: "" as string,
    }
  },
  props: {
    revisionId: Number
  },
  methods: {
    async getUsers() {
      const response = await this.$axios.$get('/users', {params: {q: this.search}})
      this.foundUsers = [...new Set([...this.foundUsers, ...response])]
      this.loading = false
    },
    async submit() {
      console.log(this.selectedUsers)
      const response = await this.$axios.$post<InviteOnRevision>(`/revisions/${this.revisionId}/invite`, {users: this.selectedUsers})
      console.log(response)
    },
    remove(user: User) {
      const index = this.selectedUsers.indexOf(user)
      if (index >= 0) this.selectedUsers.splice(index, 1)
    }
  },
  watch: {
    search() {
      // Items have already been requested
      if (this.loading) return

      this.loading = true

      this.getUsers()
    }
  },
  computed: {
    ...mapGetters('auth', ['userId']),
    foundFilteredUsers(): SearchThroughUsers {
      return this.foundUsers.filter(user => user.id != this.userId)
    }
  }
})
</script>

<style scoped>

</style>
