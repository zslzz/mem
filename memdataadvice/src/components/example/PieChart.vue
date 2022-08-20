<template>
  <div><v-chart class="chart" :option="option" /></div>
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { ref, defineComponent } from "vue";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent
]);

export default defineComponent({
  name: "PieChart",
  components: {
    VChart
  },
  provide: {
    [THEME_KEY]: "white"
  },
  methods:{

  },
  setup() {
    const option = ref({
      title: {
        text: "预算分析(万元)",
        left: "center"
      },
      tooltip: {
        trigger: "item",
        formatter: "{a} <br/>{b} : {c} ({d}%)"
      },
      legend: {
        orient: "vertical",
        left: "left",
        data: ["预处理系统", "厌氧发酵系统", "污泥脱水系统", "污水处理系统", "沼气收集及处理系统","除臭系统","沼渣处理系统"]
      },
      series: [
        {
          name: "各系统预算",
          type: "pie",
          radius: "55%",
          center: ["50%", "60%"],
          data: [
            { value: 701.75, name: "预处理系统" },
            { value: 360, name: "厌氧发酵系统" },
            { value: 90, name: "污泥脱水系统" },
            { value: 0, name: "污水处理系统" },
            { value: 182, name: "沼气收集及处理系统" },
            { value: 235, name: "除臭系统" },
            //{ value: 1548, name: "沼渣处理系统" }
          ],
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)"
            }
          }
        }
      ]
    });

    return { option };
  }
});
</script>

<style scoped>
.chart {
  height: 40vh;
  width: 80vh;
}
body {
  margin: 0;
}
</style>