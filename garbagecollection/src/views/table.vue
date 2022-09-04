
<style lang="less" scoped>
.page {
  padding: 10px 0;
  display: flex;
  justify-content: right;
}
</style>
<template>
  <div>

    <Form ref="form" :model="formInline" :rules="ruleInline" :label-width="50">
      <Row>
        <Col span="6">
        <FormItem label="姓名" prop="name">
          <Input type="text" v-model="formInline.name" placeholder="输入姓名"> </Input>
        </FormItem>
        </Col>

        <Col span="6">
        <FormItem label="姓名" prop="age">
          <Input type="text" v-model="formInline.age" placeholder="输入年龄"></Input>
        </FormItem>
        </Col>

        <Col span="6">
        <FormItem>
          <Button type="primary" @click="handleSearch()">搜索</Button>
        </FormItem>
        </Col>
      </Row>
    </Form>

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
import { tableDataList } from '../data/tableList';

export default {
  name: "DemoTable",
  setup() {
    const columns = [{
      type: 'selection',
      width: 60,
      align: 'center'
    },
    {
      title: '姓名',
      key: 'name'
    },
    {
      title: '年龄',
      key: 'age'
    },
    {
      title: '地址',
      key: 'address'
    },
    {
      title: 'Action',
      slot: 'action',
      width: 150,
      align: 'center'
    }];
    let dataList = ref([...tableDataList]);

    let formInline = reactive({
      name: '',
      age: ''
    })

    const ruleInline = {
      name: [
        { message: '请输入用户名', trigger: 'blur' }
      ],
      age: [
        { message: '其输入年龄', trigger: 'blur' },
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
      dataList.value = tableDataList.filter((item) => {
        if (formInline.name != '' && item.name != formInline.name) {
          return;
        }
        if (formInline.age != '' && item.age != formInline.age) {
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
