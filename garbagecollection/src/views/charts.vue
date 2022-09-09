

<style lang="less" scoped>
</style>
<template>
  <div>
    <Row v-margin="20">
      更多查看：<a href="https://echarts.apache.org/zh/index.html">echarts官方文档</a>
    </Row>
    <Divider />
    <div id="myChart" style="width: 100%; height: 400px"></div>
  </div>
</template>

<script lang="ts">
import * as echarts from "echarts";
import { onMounted, nextTick } from 'vue';

export default {
  name: "DemoCharts",
  setup() {
    let myChart: echarts.EChartsType;
    onMounted(() => {
      nextTick(() => {      
        let myChart_div = document.getElementById('myChart');
        if (myChart_div) {
          //视图切换不显示问题
          myChart_div.setAttribute('_echarts_instance_', '');
          //初始化echarts实例
          myChart = echarts.init(myChart_div);
          // 指定图表的配置项和数据
          let option = {
            title: {
              text: "合作伙伴分布",
              textStyle: {
                fontSize: 16,
                fontWeight: "normal",
                lineHeight: 50,
              },
              padding: [0, 0, 0, 20],
            },
            tooltip: {
              trigger: "axis",
              axisPointer: {
                type: "shadow",
              },
            },
            grid: {
              left: "3%",
              right: "4%",
              bottom: "3%",
              containLabel: true,
            },
            xAxis: [
              {
                type: "category",
                data: [
                  "北京",
                  "天津",
                  "郑州",
                  "上海",
                  "武汉",
                  "石家庄",
                  "南京",
                ],
                axisTick: {
                  alignWithLabel: true,
                },
              },
            ],
            yAxis: [
              {
                name: "单位（个）",
                nameTextStyle: {
                  align: "left",
                  verticalAlign: "top",
                },
                type: "value",
                splitLine: { show: false },
              },
            ],
            series: [
              {
                name: "套",
                type: "bar",
                barWidth: "60%",
                data: [334, 52, 200, 300, 390, 330, 220],
                itemStyle: { normal: { color: "#2C6D9D" } },
              },
            ],
          };
          // 使用刚指定的配置项和数据显示图表。
          myChart.setOption(option);

          window.addEventListener("resize", () => {
            myChart.resize();
          });
        }
      });
    });

  },
};
</script>
