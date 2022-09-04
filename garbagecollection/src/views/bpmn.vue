<style lang="less" scoped>
.vue-flow-content {
  height: 800px;
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
      <!-- 更多查看：<a href="https://vueflow.dev/">Vue Flow官方文档</a> -->
    </Row>
    <!-- <Row v-margin="5" justify="end">
      <Space wrap>
        <Button type="info" @click="resetTransform">重置</Button>
        <Button type="info" @click="updatePos">修改属性</Button>
        <Button type="info" @click="toggleclass">修改样式</Button>
        <Button type="info" @click="logToObject">查看属性</Button>
      </Space>
    </Row> -->
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
      { id: '1', type: 'input', label: '厨余收集系统', position: { x: 250, y: 0 }, class: 'node-light' },
      { id: '2', label: '预处理系统', position: { x: 250, y: 80 }, class: 'node-light' },
      { id: '3', label: '厌氧发酵系统', position: { x: 250, y: 160 }, class: 'node-light' },
      { id: '4', label: '沼气处理系统', position: { x: 250, y: 240 }, class: 'node-light' },
      { id: '5', label: '污水处理系统', position: { x: 250, y: 320 }, class: 'node-light' },
      { id: '6', label: '油气锅炉', position: { x: 450, y: 150 }, class: 'node-light' },
      { id: '7', label: '除臭系统系统', position: { x: 450, y: 250 }, class: 'node-light' },
      { id: '8', label: '自控系统', position: { x: 450, y: 55 }, class: 'node-light' },
      { id: '9', type: 'output',label: '焚烧厂', position: { x: 50, y: 200 }, class: 'node-light' },
      { id: 'e1-2', source: '1', target: '2', animated: true },
      { id: 'e2-3', source: '2', target: '3', animated: true },
      { id: 'e2-7', source: '2', target: '7', animated: true },
      { id: 'e2-9', source: '2', target: '9', animated: true ,label: "粗渣"},
      { id: 'e3-9', source: '3', target: '9', animated: true ,label: "沼渣"},
      { id: 'e3-4', source: '3', target: '4', animated: true },
      { id: 'e4-5', source: '4', target: '5', animated: true},
      { id: 'e2-3', source: '2', target: '3', animated: true},
      { id: 'e4-6', source: '4', target: '6', animated: true},
      { id: 'e5-7', source: '5', target: '7', animated: true},
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
