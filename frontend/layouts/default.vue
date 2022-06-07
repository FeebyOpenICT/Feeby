<template>
  <v-app>
    <!-- App bar -->
    <v-app-bar clipped-left fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>
        <v-btn class="btn-fix" x-large to="/" link depressed> Feeby </v-btn>
      </v-toolbar-title>
    </v-app-bar>

    <!-- Navigation drawer -->
    <v-navigation-drawer v-model="drawer" app fixed clipped>
      <!-- Title -->
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6"> Feeby </v-list-item-title>
          <v-list-item-subtitle> Instituut voor rechten </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>

      <!-- Avatar -->
      <AvatarAndName
        :canvas_email="user.canvas_email"
        :fullname="user.fullname"
        link
        to="/me"
        v-if="isAuthenticated"
      />

      <v-divider></v-divider>

      <!-- Links -->
      <v-list nav dense>
        <v-list-item link to="/">
          <v-list-item-icon>
            <v-icon>mdi-folder</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Beroepsproducten</v-list-item-title>
        </v-list-item>
        <v-list-item link to="/shared">
          <v-list-item-icon>
            <v-icon>mdi-account-multiple</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Gedeeld</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Main content -->
    <v-main class="grey lighten-2">
      <v-container fluid>
        <Nuxt keep-alive />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'DefaultLayout',
  data() {
    return {
      drawer: false,
    }
  },
  computed: {
    ...mapGetters('auth', ['isAuthenticated']),
    user() {
      return this.$store.state.auth.user
    },
  },
}
</script>

<style scoped>
.btn-fix::before {
  opacity: 0;
}
</style>
