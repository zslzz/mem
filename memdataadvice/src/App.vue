<template>
  <div class="chart-div">
    <LineTable></LineTable>
    <PieChart></PieChart>
  </div>
</template>

<script>
import PieChart from './components/example/PieChart.vue'
import LineTable from './components/example/LineTable.vue'
export default {
  name: 'App',
  components: {
    PieChart,
    LineTable
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}
</style>
