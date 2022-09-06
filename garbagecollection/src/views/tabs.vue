

<style lang="less" scoped>
</style>
<template>
  <div>
    <Tabs value="name1">
      <TabPane :label="label" name="baseInfo">
        项目名称：XX市餐厨垃圾处理项目（工艺及设备）<br/>
建设地点：XX新城产业集聚区<br/>
占地面积：约 25 亩<br/>
建设规模：XX市餐厨垃圾处理规模为50 t/d，其中，土建按照50t/d规模已经一次性全部建成（土地预留二期50t/d厨余垃圾生产线空间）。<br/>
工程内容：XX市餐厨垃圾处理项目含核心餐饮垃圾处理工程（包括预处理工艺+CSTR厌氧消化工艺+沼气净化及利用系统工艺）和配套污水处理工艺（预处理系统+两级A/O池+MBR+竖流沉淀池+活性砂虑器），除臭工艺采用“化学洗涤+生物除臭+植物液喷淋”的组合式除臭工艺。

      </TabPane>
      <TabPane label="厨余垃圾成分分析" name="name2">    
        <Row>
      <img src="../images/foodwasteanalysis.png" style="width:80%" />
        </Row>
      </TabPane>
      <TabPane label="预处理系统工作流程与物料" name="name3">
        <Row align='center'>
      <img src="../images/pre-workflow.png" style="height:60%"  />
        </Row>
      </TabPane>
      <TabPane label="厌氧发酵系统工作流程" name="fajiao">
        <Row align='center'>
      <img src="../images/fajiao-workflow.png" style="height:60%"  />
        </Row>
      </TabPane>
      <TabPane label="沼气净化系统" name="zhaoqi">
<p>本项目一期餐厨垃圾处理规模为 100 t/d，二期增设厨余垃圾处理50t/d，沼气净化处理系统一次建成。<br/> 本工程沼气从厌氧系统产出后，经过储存、脱硫、脱水、除尘、后送至过锅炉房利用。本系统设计内容是 650Nm3/h 的沼气净化系统，同时包括 1000 m3 双膜储气柜和700 Nm3/h 的沼气燃烧高空密闭式火炬系统。
   </p>    
   <Row align='center'>
      <img src="../images/zhaoqi.png" style="height:60%"  />
        </Row>
     </TabPane>
      <TabPane label="污水处理系统" name="wushui">
        <p>厌氧出水经沼渣提升泵提升至沼渣脱水离心机，污水流入渗滤液池，而后提升至气浮池。
          <br/>因餐厨垃圾沼液中还有少量的油和 SS，油脂进入生化系统后长期累积会在生物表面形成油脂包裹体，形象生化反应效果，为保证生化系统长期稳定运行，在沼液进入系统的最前段设置气浮池，对油脂和悬浮物等进行去除。</p>
      </TabPane>
      <TabPane label="臭气处理系统" name="chouqi">
<p>臭气来源主要有：餐厨预处理车间，主要为卸料间、预处理车间、出渣间、高温蒸煮罐等；<br/>餐厨预处理车间外其他区域的臭气来源主要为调节池、污泥池、污泥脱水间及污泥出渣间等</p>
<Row align='center'>
      <img src="../images/chuchou.png" style="height:60%"  />
        </Row>      
</TabPane>
      <TabPane label="干化系统" name="ganhua">          
          <p>本项目的沼渣处理工艺：沼渣浓缩池—沼渣贮池—离心脱水机—沼渣干化设备—出料螺旋输送机—冷却螺旋输送机—勾臂车厢。</p>
          <br/>
          <p>其中沼渣干化设备—出料螺旋输送机—冷却螺旋输送机为本项目预采购系统</p>
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
        h('span', '项目基本情况'),
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
