
<style lang="less" scoped>
  .page {
    padding: 10px 0;
    display: flex;
    justify-content: right;
  }
  </style>
  <template>
    <div>
  
      <Table border ref="selection" :columns="columns" :data="dataList">
        <template #name="{ row }">
          <strong>{{ row.name }}</strong>
        </template>
        <template #action="{ row, index }">
          <Button type="primary" size="small" style="margin-right: 5px" @click="show(row)">查看</Button>
          <Button type="error" size="small" @click="remove(index)">删除</Button>
        </template>
      </Table>
      <Row class="page">
        <Page :total="100" show-sizer show-elevator />
      </Row>
    </div>
  </template>
  
  <script lang="ts">
  import { Message } from 'view-ui-plus'
  import { reactive, ref } from 'vue';
  import { deviceResult1 } from '../data/tableList';
  
  export default {
    name: "deviceselector",
    setup() {
      const columns = [{
        type: 'selection',
        width: 60,
        align: 'center'
      },
      {
        title: '设备名称',
        key: 'device'
      },
      {
        title: '单位',
        key: 'measure'
      },
      {
        title: '数量',
        key: 'count'
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
        title: 'Action',
        slot: 'action',
        width: 150,
        align: 'center'
      }];
      let dataList = ref([...deviceResult1]);
  
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
        handleSearch
      }
    },
  };
  </script>
  