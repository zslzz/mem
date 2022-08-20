import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import * as echarts from "echarts"

const AppBase = createApp(App);
AppBase.use(ElementPlus)
AppBase.config.globalProperties.echarts = echarts;
AppBase.mount('#app');
