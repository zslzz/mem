<script lang="ts">
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { userStore } from "../../stores/counter";

export default {
  name: "DemoLogin",
  setup() {
    // 获取store
    const store = userStore();
    const router = useRouter();
    const loginFormRules = {
      loginName: [{ required: true, message: "不能为空", trigger: "blur" }],
      password: [{ required: true, message: "不能为空", trigger: "blur" }],
    }
    let formData = reactive({
      loginName: "admin",
      password: "123456",
    });

    const register = () => {
      router.push("/register");
    }

    const resetPassword = () => {
      router.push("/resetPassword");
    }

    let loginForm = ref();
    const handleSubmit = () => {
      if (loginForm) {
        loginForm.value.validate((valid: boolean) => {
          if (!valid) return;
          store.setLoginUser(formData.loginName);
          sessionStorage.setItem('token', formData.loginName);
          store.loadMenu();
          router.push("/home");
        });
      }
    }

    return {
      loginForm,
      formData,
      loginFormRules,
      register,
      resetPassword,
      handleSubmit
    };
  },
};
</script>

<template>
  <div class="login" @keydown.enter="handleSubmit()">
    <div class="login-bg">
      <div class="login-ctn">
        <Form ref="loginForm" :model="formData" :rules="loginFormRules" class="login-form" :label-width="50">
          <div class="login-logo">
            <img src="../../images/logo.png" alt="系统管理平台" />
          </div>

          <FormItem label="账号:" prop="loginName">
            <Input v-model="formData.loginName" class="input" placeholder="请输入账号" />
          </FormItem>

          <FormItem label="密码:" prop="password">
            <Input v-model="formData.password" type="password" class="input" placeholder="请输入密码" />
          </FormItem>

          <Row class="row-regist">
            <span @click="register()">用户注册</span>
            <span @click="resetPassword()">忘记密码</span>
          </Row>
          <Row class="row-button">
            <Button type="primary" class="button" @click="handleSubmit()">登录</Button>
          </Row>
        </Form>
      </div>
    </div>
  </div>
</template>
<style lang="less" scoped>
@import './login.less';
</style>