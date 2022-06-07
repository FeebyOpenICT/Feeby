<template>
  <v-chip pill :color="color">{{ capitalizedTitle }}</v-chip>
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
        1: '#E57373',
        2: '#F06292',
        3: '#BA68C8',
        4: '#9575CD',
        5: '#7986CB',
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
