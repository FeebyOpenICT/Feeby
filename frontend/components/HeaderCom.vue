<template>
  <v-card class="menu">
    <v-app-bar color="#0079CF">
      <v-app-bar-nav-icon class="navIcon" @click="modal = true" />
      <v-toolbar-title>FEEBY</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer
      v-model="modal"
      absolute
      temporary
      width="40vw"
      height="100vh"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            FEEBY
          </v-list-item-title>
          <v-list-item-subtitle>
            Test Menu
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider />

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
export default {
  name: 'HeaderCom',
  data: () => ({
    modal: false,
    items: [
      { title: 'Profiel', icon: 'mdi-account' },
      { title: 'Toegang Beheer', icon: 'mdi-pencil' }
    ]
  })
}
</script>

<style scoped>
.navIcon{
  position: absolute;
  right: 2%;
}
.menu {
    overflow: visible;
    top: 0;
    position: sticky;
    z-index: 2;
    border-radius: 0;
  }
</style>
