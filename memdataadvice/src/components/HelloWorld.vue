<template>
  <VueFlow>...</VueFlow>
  <WorkFlowTable></WorkFlowTable>
  <ResultTable></ResultTable>
  <LineTable></LineTable>
  <PieChart></PieChart>
  <div>
    <p>
      <b>配置总得分：80/100</b>
    </p>
  </div>
</template>
<script>
import PieChart from './example/PieChart.vue'
import LineTable from './example/LineTable.vue'
import ResultTable from './mem/ResultTable.vue'
import WorkFlowTable from './mem/WorkFlowTable.vue'
import VueFlow from './mem/VueFlow.vue'
export default {
  name: 'HelloWorld',
  components: {
    PieChart,
    LineTable,
    ResultTable,
    WorkFlowTable,
    VueFlow
},
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
