<template>
  <v-chip pill :color="color" text-color="white">{{ capitalizedTitle }}</v-chip>
</template>

<script>
export default {
  data() {
    return {}
  },
  props: {
    title: String,
    id: { type: Number, required: true },
  },
  computed: {
    color() {
      const colors = {
        1: '#9575CD',
        2: '#F06292',
        3: '#7986CB',
        4: '#E57373',
        5: '#BA68C8',
        6: '#64B5F6',
      }
      console.log('' + this.id)
      return colors['' + this.id]
    },
    capitalizedTitle() {
      return this.title.charAt(0).toUpperCase() + this.title.slice(1)
    },
  },
}
</script>
