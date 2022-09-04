<style lang="less" scoped>
</style>
<template>
  <div>
    <Row>
      <Title>ICON使用方法</Title>
    </Row>
    <Row>
      <Text v-font="16">使用Icon组件，指定图标对应的 type 属性，示例代码：</Text>
    </Row>
    <Row>
      <Text type="danger">
        <Icon type="ios-alert" />&lt;Icon type="ios-alert" /&gt;
      </Text>
    </Row>
    <Row>
      <Text v-font="16">渲染后为：</Text>
    </Row>
    <Row>
      <Text type="danger">&lt;i class="ivu-icon ivu-icon-ios-alert"&gt;&lt;/i&gt;</Text>
    </Row>
    <Row>
      <Text type="warning">更多：<a :href="link">view ui官方Icon组件</a></Text>
    </Row>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';

export default {
  name: "DemoIcon",
  setup() {
    let link = ref("https://iviewui.com/view-ui-plus/component/base/icon");
    return {
      link
    }
  },
};
</script>
