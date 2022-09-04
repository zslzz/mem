

<style lang="less" scoped>
</style>
<template>
  <div>
    <Divider>鉴权</Divider>
    <Auth :authority="authority">
      <Alert type="success">admin权限通过时显示</Alert>
      <template #noMatch>
        <Alert type="error">其他权限通过时显示</Alert>
      </template>
    </Auth>
    <Divider>测试登录</Divider>
    <Row>
      <DescriptionList :title="'不同用户登录'" :col="1">
        <Description term="">使用<router-link to="/login">admin/123456</router-link>登录</Description>
        <Description term="">使用<router-link to="/login">other/123456</router-link>登录</Description>
      </DescriptionList>
    </Row>
    <Divider></Divider>
    <Text>更多查看：<a href="https://iviewui.com/view-ui-plus/component/other/auth">官方文档</a></Text>
  </div>
</template>

<script lang="ts">
import { userStore } from "../stores/counter";

export default {
  name: "DemoPermission",
  setup() {
    // 获取store
    const store = userStore();
    const authority = () => {
      if (store.loginUser == "admin") {
        return true;
      } else {
        return false;
      }
    }
    return {
      authority
    }
  },
};
</script>
