

<style lang="less" scoped>
</style>
<template>
  <div>
    <Tabs value="name1">
      <TabPane :label="label" name="name1">标签一的内容</TabPane>
      <TabPane label="标签二" name="name2">标签二的内容</TabPane>
      <TabPane label="标签三" name="name3">标签三的内容</TabPane>
    </Tabs>
  </div>
</template>

<script lang="ts">
import { resolveComponent } from 'vue';

export default {
  name: "DemoTabs",
  setup() {
    const label = (h: any) => {
      return h('div', [
        h('span', '标签一'),
        h(resolveComponent('Badge'), {
          count: 3
        })
      ])
    }
    return {
      label
    }
  },
};
</script>
