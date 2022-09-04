
<script lang="ts">
import { ref } from 'vue';
export default {
  name: "DemoError404",
  setup() {
    let pageType = ref('404')
    return {
      pageType
    };
  }
}
</script>
<template>
  <div>
    <Exception :type="pageType" />
  </div>
</template>
<style lang="less" scoped>
</style>

