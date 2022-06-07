<template>
  <v-card>
    <v-card-title>
      <AvatarAndName
        :canvas_email="user.canvas_email"
        :fullname="user.fullname"
      />
    </v-card-title>
    <v-card-text>
      <v-chip-group>
        <RoleChip
          v-for="role in user.roles"
          :key="role.id"
          :title="role.title"
          :id="role.id"
        />
      </v-chip-group>
      Deze pagina bevat alle persoonlijke data die wij van u op het gegeven
      moment hebben.
    </v-card-text>
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Data</th>
            <th class="text-left"></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Fullname</td>
            <td>{{ user.fullname }}</td>
          </tr>
          <tr>
            <td>Internal Id</td>
            <td>{{ user.id }}</td>
          </tr>
          <tr>
            <td>Canvas Email</td>
            <td>{{ user.canvas_email }}</td>
          </tr>
          <tr>
            <td>Canvas Id</td>
            <td>{{ user.canvas_id }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </v-card>
</template>

<script>
export default {
  middleware: ['authenticated'],
  computed: {
    user() {
      return this.$store.state.auth.user
    },
  },
}
</script>
