<template>
  <div>
    <el-button type="primary" @click="choose(1)">傻瓜模式</el-button>
    <el-button type="primary" @click="choose(0)">选择模式</el-button>
    <el-button type="primary" @click="choose(2)">专家模式</el-button>
  </div>
  <HelloWorld v-if="isShow"></HelloWorld>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
// import PieChart from './components/example/PieChart.vue'
// import LineTable from './components/example/LineTable.vue'
// import ResultTable from './components/mem/ResultTable.vue'
import HelloWorld from './components/HelloWorld.vue'
// import ResultTable from './components/mem/ResultTable.vue'
export default {
  name: 'App',
  components: {
    HelloWorld
    },
    methods:{
      choose(index) {
        if(index==1){
          alert("已生成傻瓜"+"模式");
        }else if(index==2){
          alert("已生成专家"+"模式");
        }else{
          alert("请重新选择"+"模式");
        }
        if(index>0){
              this.isShow=true
        }else{
          this.isShow=false
        }
}
    },
  data() {
    return {
            isShow:false,
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
    }
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
  margin-top: 60px;
}
</style>
