<template>
  <v-data-iterator
    :sort-by="sortBy"
    :sort-desc="sortDesc"
    hide-default-footer
  >
    <template #header>
      <v-toolbar
        dark
        color="blue darken-3"
        class="mb-1"
      >
        <template v-if="$vuetify.breakpoint.mdAndUp">
          <v-spacer />
          <v-btn-toggle
            v-model="sortDesc"
            mandatory
          >
            <v-btn
              large
              depressed
              color="blue"
              :value="false"
            >
              <v-icon>mdi-arrow-up</v-icon>
            </v-btn>
            <v-btn
              large
              depressed
              color="blue"
              :value="true"
            >
              <v-icon>mdi-arrow-down</v-icon>
            </v-btn>
          </v-btn-toggle>
        </template>
      </v-toolbar>
    </template>
  </v-data-iterator>
</template>
<script>
export default {
  name: 'SearchSortBar',
  data () {
    return {
      search: '',
      filter: {},
      sortDesc: false,
      sortBy: 'date',
      keys: [
        'Title',
        'Date',
        'ID'
      ],
      lists: [
        { id: 1, title: 'test1', date: '11-03-2022' },
        { id: 2, title: 'test2', date: '14-03-2022' },
        { id: 3, title: 'test3', date: '17-02-2022' }
      ]
    }
  },
  computed: {
    filteredKeys () {
      return this.keys.filter(key => key !== 'Title')
    }
  }
}
</script>
