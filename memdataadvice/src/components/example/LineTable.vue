<template>
    <div>各个系统处理能力水平(/t)</div>
    <v-chart class="lineChart" :option="barOption" />
        <div>处理速度预估(/d)</div>
    <!-- <div id="lineTable"></div> -->
    <v-chart class="chart" :option="option" />
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import {
    TitleComponent,
    TooltipComponent,
    LegendComponent
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { ref, defineComponent } from "vue";

use([
    CanvasRenderer,
    TitleComponent,
    TooltipComponent,
    LegendComponent
]);

export default defineComponent({
    name: "LineComponent",
    components: {
        VChart
    },
    provide: {
        [THEME_KEY]: "white"
    },
    setup() {
        const option = ref({
            xAxis: {
                data: ["第1天", "第2天", "第3天", "第4天", "第5天", "第6天", "第7天"]
            },
            yAxis: {},
            series: [
                {
                    name: "用户量",
                    type: "line",
                    data: [20, 25, 28, 30,],
                    itemStyle: {
                        normal: {
                            lineStyle: {
                                width: 1
                            }
                        }
                    },
                },
                {
                    name: "用户量",
                    type: "line",
                    data: [null, null, null, 30, 32, 33, 34],
                    itemStyle: {
                        normal: {
                            lineStyle: {
                                width: 1,
                                type: 'dotted'
                            }
                        }
                    },
                    markLine: {
                        animation: true,
                        symbol: '',
                        precision: 3,
                        data: [
                            {
                                name: 'max',
                                yAxis: 33,
                                symbol: '',
                                lineStyle: { 
                                    normal: {
                                        color: 'red',
                                        width: 1, // 线宽
                                        type: 'dashed'
                                    }
                                },
                                label: {
                                    normal: {
                                        show: false,
                                        position: 'middle',
                                        formatter: '{b}: {c}'
                                    }
                                }
                            }]
                    }
                },

            ]
        });
        const barOption = ref({
            xAxis: {
                data: ["预处理系统", "厌氧发酵系统", "污泥脱水系统", "污水处理系统", "沼气收集及处理系统", "除臭系统", "沼渣处理系统"]
            },
            yAxis: {},
            series: [
                {
                    name: "处理能力",
                    type: "bar",
                    data: [8, 15, 31, 13, 15, 22, 11]
                }
            ]
        })
        return { option, barOption };
    }
});
</script>

<style scoped>
.chart {
    height: 30vh;
    width: 100vh;
}
.lineChart {
    height: 30vh;
    width: 150vh;
}

body {
    margin: 0;
}
</style>