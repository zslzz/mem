<template>
  <div id="app">
      <workflow-chart
          :transitions="transitions"
          :states="states" />
  </div>
</template>

<script>
import WorkflowChart from 'vue-workflow-chart';

export default {
  name: "App",
  components: {
      WorkflowChart,
  },
  data: () => ({
      states: [{
          "id": "state_1",
          "label": "State 1",
      }, {
          "id": "state_2",
          "label": "State 2",
      }],
      transitions: [{
          "id": "transition_1",
          "label": "this is a transition",
          "target": "state_2",
          "source": "state_1",
      }],
  }),
};
</script>