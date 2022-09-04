<style lang="less" scoped>
</style>
<template>
  <div>
    <Row>
      通过切换语言按钮，来改变当前内容的语言。
      <Button type="primary" @click="changeLang()" size="small">切换语言</Button>
    </Row>
    <Divider>text</Divider>
    <Row>
      <DescriptionList :title="t('oldManAndSea.title')" :col="1">
        <Description term="1.">{{t('oldManAndSea.famous[0]')}}</Description>
        <Description term="2.">{{t('oldManAndSea.famous[1]')}}</Description>
        <Description term="3.">{{t('oldManAndSea.famous[2]')}}</Description>
        <Description term="4.">{{t('oldManAndSea.famous[3]')}}</Description>
        <Description term="5.">{{t('oldManAndSea.famous[4]')}}</Description>
      </DescriptionList>
    </Row>
    <Divider>text</Divider>
    <Row>
      相关文档：
      <a href="https://iviewui.com/view-ui-plus/guide/i18n">view ui vue-i18n配置</a>
      &nbsp;&nbsp;&nbsp;
      <a href="https://vue-i18n.intlify.dev/guide/migration/vue3.html#how-to-migration">vue3 vue-i18n配置</a>
    </Row>
  </div>
</template>

<script lang="ts">
import { useI18n } from 'vue-i18n'
import type { ComponentInternalInstance } from 'vue';
import { getCurrentInstance } from 'vue';

export default {
  name: "DemoI18n",
  setup() {
    const { t } = useI18n();
    const { proxy } = (getCurrentInstance() as ComponentInternalInstance)
    const changeLang = () => {
      if (proxy) {
        if (proxy.$i18n.locale == 'zh-CN') {
          proxy.$i18n.locale = 'en-US';
        } else {
          proxy.$i18n.locale = 'zh-CN';
        }
      }
    }
    return {
      t,
      changeLang
    }
  },
};
</script>
