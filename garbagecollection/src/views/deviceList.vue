
<style lang="less" scoped>
.page {
  padding: 10px 0;
  display: flex;
  justify-content: right;
}
</style>
<template>
  <div>
    <div id="printMe" class="print-area">
      <Form ref="form" :model="formInline" :rules="ruleInline" :label-width="100">
      <Row>
        <Col span="5">
        <FormItem label="名称" prop="name">
          <Input type="text" v-model="formInline.name" placeholder="接料装置"> </Input>
        </FormItem>
        </Col>

        <Col span="4">
        <FormItem label="价格（万元）" prop="value">
          <Input type="text" v-model="formInline.value" placeholder="40"></Input>
        </FormItem>
        </Col>

        <Col span="6">
        <FormItem>
          <Button type="primary" @click="handleSearch()">搜索</Button>
        </FormItem>
        </Col>
      </Row>
    </Form>

      <Table striped border ref="selection" :columns="columns" :data="dataList">
        <template #name="{ row }">
          <strong>{{ row.name }}</strong>
        </template>
        <template #action="{ row, index }">
          <Button type="primary" size="small" style="margin-right: 5px" @click="show(row)">详情</Button>
          <Button type="error" size="small" @click="remove(index)">删除</Button>
        </template>
      </Table>
    </div>
    <Row class="page">
      <Page :total="100" show-sizer show-elevator />
    </Row>
  </div>
</template>
    
<script lang="ts">
import { Alert, Message } from 'view-ui-plus'
import { reactive, ref,onMounted } from 'vue';
import { deviceResult1 } from '../data/tableList';
import print from 'vue3-print-nb';
import axios from 'axios'

export default {
  name: "deviceList",
  directives: {
    print
  },
  setup() {
    const columns = [
    {
      title: '装置',
      key: '装置'
    },
    {
      title: '参数',
      key: '参数'
    },
    {
      title: '材质',
      key: '材质'
    },
    {
      title: '价格（万元）',
      key: '价格（万元）'
    },
    {
      title: '厂家',
      key: '厂家',
      width: 250,
    },
    {
      title: 'Action',
      slot: 'action',
      width: 150,
      align: 'center'
    }];
    let dataList = ref([...deviceResult1]);

    let printLoading = ref(true);
    let formInline = reactive({
      name: '',
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

    const handleSearch = () => {
      // dataList.value = deviceResult1.filter((item) => {
      //   if (formInline.name != '' && item.name != formInline.name) {
      //     return;
      //   }
      //   if (formInline.value != '' && item.value != formInline.value) {
      //     return;
      //   }
      //   return item;
      // });
      alert("这个功能还在开发，请等待")
    }


    onMounted(() => {
      var url = '/api/all' 
      axios.get(url)
        .then(response => {
          //   this. = response.data;
          dataList.value =response.data;
          console.log(dataList.value);
        })
        .catch(error => {
          console.log(error);
        });
      
    })

    return {
      columns,
      dataList,
      show,
      selection,
      formInline,
      ruleInline,
      handleSearch,
      printLoading
    }
  },
};
</script>
    