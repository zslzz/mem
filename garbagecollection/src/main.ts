import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';
import ViewUIPlus from 'view-ui-plus';
import { i18n } from './i18n';
//import print from 'vue3-print-nb';
import 'view-ui-plus/dist/styles/viewuiplus.css';
import './styles/my-theme/index.less';

const app = createApp(App);
app.use(createPinia());
app.use(router);
app.use(i18n).use(ViewUIPlus, { i18n });
// app.use(print);
app.mount('#app');
