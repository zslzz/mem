<template>
  <VueFlow/>
  <!-- <div>
    <el-button type="primary" @click="choose(1)">简易模式</el-button>
    <el-button type="primary" @click="choose(0)">重新选择模式</el-button>
    <el-button type="primary" @click="choose(2)">专家模式</el-button>
  </div>
  <HelloWorld v-if="isShow"></HelloWorld> -->
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import VueFlow from './components/mem/VueFlow.vue';
// import ResultTable from './components/mem/ResultTable.vue'
export default {
  name: 'App',
  components: {
    // HelloWorld,
    VueFlow
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
            isShow:false
    }
  }
}
</script>

<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  /* -webkit-font-smoothing: antialiased; */
  /* -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  /* color: #2c3e50; */
  /* margin-top: 60px; */
  justify-content: center;
  padding-top: 100px;
}
</style>
