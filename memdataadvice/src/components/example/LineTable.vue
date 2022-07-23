<template>
    <div>lineTable</div>
    <div id="lineTable"></div>
    <v-chart class="chart" :option="option" />
    <v-chart class="chart" :option="barOption" />
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
        [THEME_KEY]: "dark"
    },
    setup() {
        const option = ref({
            xAxis: {
                data: ["4-3", "4-4", "4-5", "4-6", "4-7", "4-8", "4-9"]
            },
            yAxis: {},
            series: [
                {
                    name: "用户量",
                    type: "line",
                    data: [8, 15, 31, 13,],
                    itemStyle: {
                        normal: {
                            lineStyle: {
                                width: 5
                            }
                        }
                    },
                },
                {
                    name: "用户量",
                    type: "line",
                    data: [null, null, null, 13, 15, 22, 11],
                    itemStyle: {
                        normal: {
                            lineStyle: {
                                width: 5,
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
                                yAxis: 18,
                                symbol: '',
                                lineStyle: { 
                                    normal: {
                                        color: 'red',
                                        width: 5, // 线宽
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
                data: ["4-3", "4-4", "4-5", "4-6", "4-7", "4-8", "4-9"]
            },
            yAxis: {},
            series: [
                {
                    name: "用户量",
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

body {
    margin: 0;
}
</style>