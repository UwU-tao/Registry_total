<template>
  <div>
    <h1>Dashboard</h1>
    <DataTable />
  </div>
</template>

<script>
import { collapsed, toggleSidebar } from '@/components/sidebar/state'
import DataTable from '@/components/DataTable.vue'

export default {
  setup() {
    return { collapsed, toggleSidebar}
  },
  components: {
    DataTable
  }
}
</script>

<style scoped>
  * {
    text-align: center;
  }
</style>