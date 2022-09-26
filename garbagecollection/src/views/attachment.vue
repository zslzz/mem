

<style lang="less" scoped>
</style>
<template>
  <div>
    nnn
    <Tabs value="name1">
      <TabPane :label="label" name="baseInfo">
          主要显示各子系统的设备参数等
      </TabPane>
      <TabPane label="预处理系统清单" name="name3">
        <Row align='center'>
      <img src="../images/prea.png" style="width:80%"  />
        </Row>
      </TabPane>
      <TabPane label="厌氧发酵系统清单" name="fajiao">
        <Row align='center'>
      <img src="../images/yanyanga.png" style="width:80%"  />
        </Row>
      </TabPane>

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
        h('span', '设备清单'),
        h(resolveComponent('Badge'), {
          count: 1
        })
      ])
    }
    return {
      label
    }
  },
};
</script>
