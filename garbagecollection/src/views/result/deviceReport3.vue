
<style lang="less" scoped>
  .page {
    padding: 10px 0;
    display: flex;
    justify-content: right;
  }
  </style>
  <template>
    <div>
      <Row>
      <Button type="primary" size="small" v-print="printObj">打印</Button>
      <div id="loading" v-show="printLoading"></div>
    </Row>
    <Divider></Divider>
    <div id="printMe" class="print-area">
      <Table striped border ref="selection" :columns="columns" :data="dataList">
        <template #name="{ row }">
        <strong>{{ row.name }}</strong>
        </template>
        <template #action="{ row, index }">
          <Button type="primary" size="small" style="margin-right: 5px" @click="show(row)">详情</Button>
        </template>
      </Table>
      </div>
      <Divider></Divider>
      <Row class="page">
        <Page :total="100" show-sizer show-elevator />
      </Row>
    </div>
  </template>
  
  <script lang="ts">
  import { Message } from 'view-ui-plus'
  import { reactive, ref } from 'vue';
  import { deviceResult1 } from '../../data/tableList';
  import print from 'vue3-print-nb';
  export default {
    name: "deviceReport3",
    directives: {
    print
    },
    methods:{
    // cellStyle(row,column,rowIndex,columnIndex){
    //      console.log(row,column,rowIndex,columnIndex)
    //        if (row.seq == '10' ||row.seq == '11'|| row.seq == '13') {
    //            return `font-weight:bolder!important;`;
    //         } else {
    //              return ''
    //         }
    //       }
    //  
     },
    setup() {
      const columns = [
      {
        title: '设备名称',
        key: 'device'
      },
      {
        title: '单价（万）',
        key: 'value'
      },
      {
        title: '总价（万）',
        key: 'totalValue'
      },
      {
        title: '数量',
        key: 'count'
      },
      {
        title: '单位',
        key: 'measure'
      },
      {
        title: 'Action',
        slot: 'action',
        width: 150,
        align: 'center'
      }];
      let dataList = ref([...deviceResult1]);
  
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
    });
      let formInline = reactive({
        device: '',
        value: ''
      })
  
      const ruleInline = {
        device: [
          { message: '请输入设备名称', trigger: 'blur' }
        ],
        value: [
          { message: '请输入金额', trigger: 'blur' },
          // { type: 'number', max: 3, message: '年龄必须是数字', trigger: 'blur' }
        ]
      }
  
      let selection = ref();
      const show = (row: object) => {
        Message.info(JSON.stringify(row));
      }
      const remove = (index: number) => {
        dataList.value.splice(index, 1);
      }
      const handleSearch = () => {
        dataList.value = deviceResult1.filter((item) => {
          if (formInline.device != '' && item.device != formInline.device) {
            return;
          }
          if (formInline.value != '' && item.value != formInline.value) {
            return;
          }
          return item;
        });
      }
  
      return {
        columns,
        dataList,
        show,
        remove,
        selection,
        formInline,
        ruleInline,
        handleSearch,
        printObj,
        printLoading
      }
    },
  };
  </script>
  