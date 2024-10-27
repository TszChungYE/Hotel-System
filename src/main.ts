import { createApp } from 'vue';
import App from './App.vue'; //导入应用的主组件，通常是 App.vue。
import router from './router'; //导入应用的路由配置。
import piniaStore from './store'; //导入应用的状态管理

import bootstrap from './core/bootstrap';
import '/@/styles/reset.less';
import '/@/styles/index.less';
import Antd from 'ant-design-vue';

//使用 createApp 函数创建一个 Vue 应用实例，该实例可以配置和挂载到 HTML 页面上。
const app = createApp(App);

//使用 Vue 插件，将 Ant Design Vue、路由、状态管理、自定义逻辑等集成到应用中。
app.use(Antd);
app.use(router);
app.use(piniaStore);
app.use(bootstrap)
app.mount('#app'); //将应用实例挂载到页面上的 #app 元素上，这个元素通常是在 HTML 文件中定义的应用容器。

