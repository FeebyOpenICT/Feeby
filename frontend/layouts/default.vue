<template>
  <v-app>
    <!-- Navigation drawer -->
    <v-navigation-drawer
      permanent
      expand-on-hover
      app
      floating
      mini-variant
      style="border-right: 1px solid grey"
    >
      <!-- Title -->
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6"> Feeby </v-list-item-title>
          <v-list-item-subtitle> Instituut voor rechten </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>

      <!-- Avatar -->
      <v-list>
        <v-list-item class="px-2">
          <v-list-item-avatar>
            <v-img src="https://hboi.lucabergman.com/fotovanmij.jpeg"></v-img>
          </v-list-item-avatar>
        </v-list-item>
        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="text-h6">
              Luca Bergman
            </v-list-item-title>
            <v-list-item-subtitle
              >luca.bergman@student.hu.nl</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
      </v-list>

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
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
}
</script>
