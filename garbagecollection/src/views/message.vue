

<style lang="less" scoped>
</style>
<template>
  <div>
    <Title v-font="20">Alert 警告提示</Title>
    <div>
      <Alert closable>An info prompt</Alert>
      <Alert type="success" show-icon closable>
        A success prompt
        <template #desc>Content of prompt. Content of prompt. Content of prompt. Content of prompt. </template>
      </Alert>
      <Alert type="warning" closable>
        Custom closing content
        <template #close>No longer prompt</template>
      </Alert>
    </div>
    <Divider />
    <Title v-font="20">Message 全局提示</Title>
    <Space wrap>
      <Button @click="background('info')">显示普通提示</Button>
      <Button @click="background('success')">显示成功提示</Button>
      <Button @click="background('warning')">显示警告提示</Button>
      <Button @click="background('error')">显示错误提示</Button>
    </Space>
    <Divider />
    <Title v-font="20">Notice 通知提醒</Title>
    <Space direction="vertical">
      <p>With desc</p>
      <Space wrap>
        <Button @click="info(false)">Info</Button>
        <Button @click="success(false)">Success</Button>
        <Button @click="warning(false)">Warning</Button>
        <Button @click="error(false)">Error</Button>
      </Space>
      <p>Only title</p>
      <Space wrap>
        <Button @click="info(true)">Info</Button>
        <Button @click="success(true)">Success</Button>
        <Button @click="warning(true)">Warning</Button>
        <Button @click="error(true)">Error</Button>
      </Space>
    </Space>
    <Divider />
    <Title v-font="20">Modal 对话框</Title>
    <div>
      <Button type="primary" @click="modal = true">弹窗</Button>
      <Modal v-model="modal" title="Common Modal dialog box title" @on-ok="ok" @on-cancel="cancel">
        <p>Content of dialog</p>
        <p>Content of dialog</p>
        <p>Content of dialog</p>
      </Modal>
    </div>
    <Divider />
    <Text>更多查看：<a href="https://iviewui.com/view-ui-plus/component/view/notice">官方文档</a></Text>
  </div>
</template>

<script lang="ts">
import { Message, Notice } from 'view-ui-plus';
import { ref } from 'vue';


export default {
  name: "DemoMessage",
  setup() {
    const background = (type: string) => {
      Message[type]({
        background: true,
        content: '这是一条带背景色的通知'
      });
    }

    const info = (nodesc: boolean) => {
      Notice.info({
        title: 'Notification title',
        desc: nodesc ? '' : 'Here is the notification description. Here is the notification description. '
      });
    }
    const success = (nodesc: boolean) => {
      Notice.success({
        title: 'Notification title',
        desc: nodesc ? '' : 'Here is the notification description. Here is the notification description. '
      });
    }
    const warning = (nodesc: boolean) => {
      Notice.warning({
        title: 'Notification title',
        desc: nodesc ? '' : 'Here is the notification description. Here is the notification description. '
      });
    }
    const error = (nodesc: boolean) => {
      Notice.error({
        title: 'Notification title',
        desc: nodesc ? '' : 'Here is the notification description. Here is the notification description. '
      });
    }

    const ok = () => {
      Message.info('Clicked ok');
    }
    const cancel = () => {
      Message.info('Clicked cancel');
    }

    let modal = ref(false)
    return {
      background,
      info,
      success,
      warning,
      error,
      modal,
      ok,
      cancel
    }
  },
};
</script>
