
<style lang="less" scoped>
</style>
<template>
  <Form ref="formRef" :model="formValidate" :rules="ruleValidate" :label-width="80">
    <FormItem label="设备名称" prop="name">
      <Input v-model="formValidate.name" placeholder="输入设备名"></Input>
    </FormItem>
    <FormItem label="设备厂家" prop="producer">
      <Input v-model="formValidate.producer" placeholder="输入品牌"></Input>
    </FormItem>
    <FormItem label="设备型号" prop="type">
      <Input v-model="formValidate.type" placeholder="输入型号"></Input>
    </FormItem>
    <FormItem label="设备价格" prop="value">
      <Input v-model="formValidate.value" placeholder="输入价格"></Input>
    </FormItem>
    <FormItem label="设备产地" prop="city">
      <Select v-model="formValidate.city" placeholder="选择城市">
        <Option value="beijing">北京</Option>
        <Option value="shanghai">上海</Option>
        <Option value="shenzhen">深圳</Option>
        <Option value="chengdu">成都</Option>
      </Select>
    </FormItem>
    <FormItem label="设备材质" prop="type">
      <RadioGroup v-model="formValidate.gender">
        <Radio label="不锈钢">不锈钢</Radio>
        <Radio label="PPE">PPE</Radio>
      </RadioGroup>
    </FormItem>
    <FormItem label="设备备注" prop="desc">
      <Input v-model="formValidate.desc" type="textarea" :autosize="{minRows: 2,maxRows: 5}"
        placeholder="备注"></Input>
    </FormItem>
    <FormItem>
      <Button type="primary" @click="handleSubmit()">提交</Button>
      <Button @click="handleReset()" style="margin-left: 8px">重置</Button>
    </FormItem>
  </Form>
</template>

<script lang="ts">
import type { Ref } from 'vue';
import { reactive, ref } from 'vue';
import { Message } from 'view-ui-plus';

export default {
  name: "DemoForm",
  setup() {

    let formValidate = reactive({
      name: '',
      mail: '',
      city: '',
      gender: '',
      interest: [],
      date: '',
      time: '',
      desc: ''
    })
    const ruleValidate = {
      name: [
        { required: true, message: '设备名不能为空', trigger: 'blur' }
      ],
      mail: [
        { required: true, message: '邮件不能为空', trigger: 'blur' },
        { type: 'email', message: '邮件格式错误', trigger: 'blur' }
      ],
      city: [
        { required: true, message: '请选择城市', trigger: 'change' }
      ],
      gender: [
        { required: true, message: '请选择性别', trigger: 'change' }
      ],
      interest: [
        { required: true, type: 'array', min: 1, message: '选择爱好', trigger: 'change' },
        { type: 'array', max: 2, message: '最多选择两个爱好', trigger: 'change' }
      ],
      date: [
        { required: true, type: 'date', message: '选择日期', trigger: 'change' }
      ],
      time: [
        { required: true, type: 'string', message: '选择时间', trigger: 'change' }
      ],
      desc: [
        {  message: '请输入设备介绍', trigger: 'blur' },
        { type: 'string', min: 20, message: '最少20个字', trigger: 'blur' }
      ]
    }

    let formRef = ref();
    const handleSubmit = () => {
      formRef.value.validate((valid: boolean) => {
        if (valid) {
          Message.success('成功!');
        } else {
          Message.error('失败!');
        }
      })
    }
    const handleReset = () => {
      formRef.value.resetFields();
    }

    return {
      formValidate,
      ruleValidate,
      formRef,
      handleSubmit,
      handleReset
    }
  },
};
</script>
