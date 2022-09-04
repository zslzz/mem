<style lang="less" scoped>
</style>
<template>
  <div>
    <Divider>环境变量</Divider>
    <Row>
      <DescriptionList :title="'环境变量'" :col="1">
        <Description term="VITE_PARAM:">{{VITE_PARAM}}</Description>
        <Description term="VITE_BASE_URL:">{{VITE_BASE_URL}}</Description>
      </DescriptionList>
    </Row>
    <Divider>环境变量</Divider>

    <Divider>配置文件</Divider>
    <Row>
      <DescriptionList :title="'配置文件'" :col="1">
        <Description term="1:">.env通用环境参数</Description>
        <Description term="2:">.env.development测试环境参数</Description>
        <Description term="3:">.env.product生产环境参数</Description>
      </DescriptionList>
    </Row>
    <Divider>配置文件</Divider>
  </div>
</template>

<script lang="ts">

export default {
  name: "DemoEnv",
  setup() {
    const VITE_PARAM = import.meta.env.VITE_PARAM;
    const VITE_BASE_URL = import.meta.env.VITE_BASE_URL;
   
    return {
      VITE_PARAM,
      VITE_BASE_URL
    }
  },
};
</script>
