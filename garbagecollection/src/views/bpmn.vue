<style lang="less" scoped>
.vue-flow-content {
  height: 400px;
  :deep(.node-light) {
    background: none;
  }
  :deep(.node-dark) {
    background: #eeeeee;
  }
}
</style>
<template>
  <div>
    <Row v-margin="5">
      更多查看：<a href="https://vueflow.dev/">Vue Flow官方文档</a>
    </Row>
    <Row v-margin="5" justify="end">
      <Space wrap>
        <Button type="info" @click="resetTransform">重置</Button>
        <Button type="info" @click="updatePos">修改属性</Button>
        <Button type="info" @click="toggleclass">修改样式</Button>
        <Button type="info" @click="logToObject">查看属性</Button>
      </Space>
    </Row>
    <VueFlow v-model="elements" class="vue-flow-content">
      <Background />
      <MiniMap />
      <Controls />
    </VueFlow>
  </div>
</template>

<script lang="ts">
import '@braks/vue-flow/dist/style.css';
import '@braks/vue-flow/dist/theme-default.css';
import type { Elements } from '@braks/vue-flow'
import { Background, Controls, MiniMap, VueFlow, isNode, useVueFlow } from '@braks/vue-flow'
import { ref } from 'vue';
import { Message } from 'view-ui-plus';

export default {
  name: "DemoBpmn",
  components: { VueFlow, Background, Controls, MiniMap },
  setup() {

    const elementsDefault = [
      { id: '1', type: 'input', label: 'Node 1', position: { x: 250, y: 5 }, class: 'node-light' },
      { id: '2', label: 'Node 2', position: { x: 100, y: 100 }, class: 'node-light' },
      { id: '3', label: 'Node 3', position: { x: 400, y: 100 }, class: 'node-light' },
      { id: '4', label: 'Node 4', position: { x: 400, y: 200 }, class: 'node-light' },
      { id: 'e1-2', source: '1', target: '2', animated: true },
      { id: 'e1-3', source: '1', target: '3' },
    ];

    const elements = ref<Elements>(elementsDefault);
    const { onPaneReady, onNodeDragStop, onConnect, addEdges, setTransform, toObject } = useVueFlow({
      defaultZoom: 1.5,
      minZoom: 0.2,
      maxZoom: 4,
    })

    onPaneReady(({ fitView }) => {
      fitView()
    })
    onNodeDragStop((e) => console.log('drag stop', e))
    onConnect((params) => addEdges([params]))

    const updatePos = () => {
      elements.value.forEach((el) => {
        if (isNode(el)) {
          el.position = {
            x: Math.random() * 400,
            y: Math.random() * 400,
          }
        }
      })
    };

    const logToObject = () => {
      Message.info(JSON.stringify(toObject()));
    };
    const resetTransform = () => {
      elements.value = elementsDefault;
      setTransform({ x: 0, y: 0, zoom: 1 })
    };
    const toggleclass = () => elements.value.forEach((el) => (el.class = el.class === 'node-light' ? 'node-dark' : 'node-light'))
    return {
      elements,
      updatePos,
      logToObject,
      resetTransform,
      toggleclass
    };
  }
};
</script>
