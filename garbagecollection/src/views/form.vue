
<style lang="less" scoped>
</style>
<template>
  <Form ref="formRef" :model="formValidate" :rules="ruleValidate" :label-width="80">
    <FormItem label="姓名" prop="name">
      <Input v-model="formValidate.name" placeholder="输入姓名"></Input>
    </FormItem>
    <FormItem label="邮件" prop="mail">
      <Input v-model="formValidate.mail" placeholder="输入邮件"></Input>
    </FormItem>
    <FormItem label="城市" prop="city">
      <Select v-model="formValidate.city" placeholder="选择城市">
        <Option value="beijing">北京</Option>
        <Option value="shanghai">上海</Option>
        <Option value="shenzhen">深圳</Option>
        <Option value="chengdu">成都</Option>
      </Select>
    </FormItem>
    <FormItem label="时间">
      <Row>
        <Col span="11">
        <FormItem prop="date">
          <DatePicker type="date" placeholder="选择日期" v-model="formValidate.date"></DatePicker>
        </FormItem>
        </Col>
        <Col span="2" style="text-align: center">-</Col>
        <Col span="11">
        <FormItem prop="time">
          <TimePicker type="time" placeholder="选择时间" v-model="formValidate.time"></TimePicker>
        </FormItem>
        </Col>
      </Row>
    </FormItem>
    <FormItem label="性别" prop="gender">
      <RadioGroup v-model="formValidate.gender">
        <Radio label="男">男</Radio>
        <Radio label="女">女</Radio>
      </RadioGroup>
    </FormItem>
    <FormItem label="爱好" prop="interest">
      <CheckboxGroup v-model="formValidate.interest">
        <Checkbox label="吃"></Checkbox>
        <Checkbox label="喝"></Checkbox>
        <Checkbox label="跑步"></Checkbox>
        <Checkbox label="羽毛球"></Checkbox>
      </CheckboxGroup>
    </FormItem>
    <FormItem label="介绍" prop="desc">
      <Input v-model="formValidate.desc" type="textarea" :autosize="{minRows: 2,maxRows: 5}"
        placeholder="输入自我介绍"></Input>
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
        { required: true, message: '姓名不能为空', trigger: 'blur' }
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
        { required: true, message: '请输入自我介绍', trigger: 'blur' },
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
