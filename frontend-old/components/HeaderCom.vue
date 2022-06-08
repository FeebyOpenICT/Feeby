<template>
  <v-card class="menu">
    <v-app-bar color="var(--blue)">
      <v-app-bar-nav-icon class="iconbtn" @click="drawer = true" />
      <v-btn to="/" nuxt class="logobtn">
        <v-toolbar-title>FEEBY</v-toolbar-title>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      class="modalmenu"
      temporary
      hide-overlay
    >
      <v-list-item>
        <v-list-item-title class="text-h6">
          FEEBY
        </v-list-item-title>
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
        <v-list-item
          to="/aspectmaken"
          nuxt
          link
        >
          <v-list-item-icon>
            <v-icon>mdi-pencil</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>Aspect Aanmaken</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          to="/adminpagina"
          nuxt
          link
        >
          <v-list-item-icon>
            <v-icon>mdi-pencil</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>Admin Pagina</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
import '../style/style.css'
export default {
  name: 'HeaderCom',
  data: () => ({
    drawer: null,
    items: [
      { title: 'Profiel', icon: 'mdi-account' },
      { title: 'Toegang Beheer', icon: 'mdi-pencil' }
    ]
  })
}
</script>

<style scoped>
.menu {
  overflow: visible;
  top: 0;
  position: sticky;
  border-radius: 0;
  z-index: 2;
}

.modalmenu{
  width: 40vw !important;
  height: 100vh !important;
  position: absolute;
}

.iconbtn{
  color: white !important;
}

.logobtn{
  background-color: var(--blue) !important;
  box-shadow: none;
  font-size: large;
  color: white;
  text-decoration: none;
}

.v-btn:hover::before {
  opacity: 0;
}

.v-btn--active::before {
  opacity: 0;
}

v-list-item-content {
  background-color: var(--blue);
}
</style>
