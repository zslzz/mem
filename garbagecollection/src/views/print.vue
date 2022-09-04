<style lang="less" scoped>
.print-area {
  max-width: 800px;
}
</style>
<template>
  <div>
    <Row>
      <Button type="primary" size="small" v-print="printObj">打印</Button>
      <div id="loading" v-show="printLoading"></div>
    </Row>
    <Divider>打印区域</Divider>
    <div id="printMe" class="print-area">
      <Table stripe :columns="columns" :data="data"></Table>
    </div>
    <Divider>打印区域</Divider>
    <Row>
      相关文档：
      <a href="https://github.com/Power-kxLee/vue-print-nb#vue3-version">vue-print-nb</a>
    </Row>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
// @ts--ignore 
import print from 'vue3-print-nb';

export default {
  name: "DemoPrint",
  directives: {
    print
  },
  setup() {
    let printLoading = ref(true);
    let printObj = ref({
      id: "printMe",
      popTitle: 'good print',
      extraCss: "https://cdn.bootcdn.net/ajax/libs/animate.css/4.1.1/animate.compat.css, https://cdn.bootcdn.net/ajax/libs/hover.css/2.3.1/css/hover-min.css",
      extraHead: '<meta http-equiv="Content-Language"content="zh-cn"/>',
      beforeOpenCallback(vue: { printLoading: boolean; }) {
        vue.printLoading = true
        console.log('打开之前')
      },
      openCallback(vue: { printLoading: boolean; }) {
        vue.printLoading = false
        console.log('打开打印页面')
      },
      closeCallback(vue: any) {
        console.log('关闭了打印工具')
      }
    })
    let columns = ref([
      {
        title: 'Name',
        key: 'name'
      },
      {
        title: 'Age',
        key: 'age'
      },
      {
        title: 'Address',
        key: 'address'
      }
    ])
    let data = ref([
      {
        name: 'John Brown',
        age: 18,
        address: 'New York No. 1 Lake Park',
        date: '2016-10-03'
      },
      {
        name: 'Jim Green',
        age: 24,
        address: 'London No. 1 Lake Park',
        date: '2016-10-01'
      },
      {
        name: 'Joe Black',
        age: 30,
        address: 'Sydney No. 1 Lake Park',
        date: '2016-10-02'
      },
      {
        name: 'Jon Snow',
        age: 26,
        address: 'Ottawa No. 2 Lake Park',
        date: '2016-10-04'
      }
    ])

    return {
      printLoading,
      printObj,
      columns,
      data
    }
  },
};
</script>
