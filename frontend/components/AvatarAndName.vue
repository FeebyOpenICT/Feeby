<template>
  <v-list>
    <v-list-item :link="link" :to="to" class="px-2">
      <v-list-item-avatar color="blue">
        <!-- Show first to letters, implement canvas image later -->
        <span class="white--text text-h5">{{
          first_two_letters_from_fullname
        }}</span>
        <!-- <v-img src="https://hboi.lucabergman.com/fotovanmij.jpeg"></v-img> -->
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title class="text-h6">
          {{ fullname }}
        </v-list-item-title>
        <v-list-item-subtitle>{{ canvas_email }}</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  name: 'AvatarAndName',
  props: {
    fullname: { type: String, required: true },
    canvas_email: { type: String, required: true },
    to: String,
    link: Boolean,
  },
  computed: {
    first_two_letters_from_fullname() {
      return this.fullname.slice(0, 2)
    },
  },
}
</script>
