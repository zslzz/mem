
<style lang="less" scoped>
.page {
  padding: 10px 0;
  display: flex;
  justify-content: right;
}
</style>
<template>
  <div>

    <Form ref="form" :model="formInline" :rules="ruleInline" :label-width="90">
      <Row>
        <Col span="5">
        <FormItem label="预算(w)" prop="budget">
          <Input type="text" v-model="formInline.budget" placeholder="1500"> </Input>
        </FormItem>
        </Col>

        <Col span="5">
        <FormItem label="处理吨数(t)" prop="ability">
          <Input type="text" v-model="formInline.ability" placeholder="50"></Input>
        </FormItem>
        </Col>

        <Col span="6">
        <FormItem>
          <Button type="primary" @click="handleSearch()">搜索</Button>
        </FormItem>
        </Col>
        <Col span="6">
        <FormItem>
          <Button type="primary" @click="showHiddenFun()">展示/隐藏 所有</Button>
        </FormItem>
        </Col>
      </Row>
    </Form>

    <Table border ref="selection" :columns="columns" :data="dataList" v-show="isShow">
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
import { reactive, ref,onMounted } from 'vue';
import { tableDataList } from '../data/tableList';
import axios from 'axios'

export default {
  name: "DemoTable",
  setup() {
    const columns = [
    {title: '报告名称',key: 'name'},
    {title: '处理量(t)',key: 'ability'},
    {title: '预算(w)',key: 'budget'},
    {title: 'Action',slot: 'action',width: 150,align: 'center'}];
    let dataList = ref([...tableDataList]);

    let formInline = reactive({
      ability: '',
      budget: ''
    })

    const ruleInline = {
      budget: [
        { message: '请输入预算', trigger: 'blur' }
      ],
      ability: [
        { message: '请输入处理量', trigger: 'blur' },
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
    
    let isShow = ref(false)
    const showHiddenFun = () => {
      isShow.value=!isShow.value
  
      var url = '/test/info' 
      url = '/api/all'
      axios.get(url)
        .then(response => {
          //   this. = response.data;
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });
    };

    const handleSearch = () => {
      dataList.value = tableDataList.filter((item) => {
        isShow.value=true
        if (formInline.budget != '' && item.budget != Number(formInline.budget)) {
          return;
        }
        if (formInline.ability != '' && item.ability != Number(formInline.ability)) {
          return;
        }
        return item;
      });
    }

   
    return {
      isShow,
      columns,
      dataList,
      showHiddenFun,
      remove,
      selection,
      formInline,
      ruleInline,
      handleSearch
    }
  },
};
</script>
