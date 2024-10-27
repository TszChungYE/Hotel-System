<template>
  <a-config-provider :locale="zhCN">
    <router-view />
  </a-config-provider>
</template>
<script setup lang="ts">

import zhCN from 'ant-design-vue/es/locale/zh_CN';

</script>

<style>

  #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  height: 100vh;
}
</style>

<!--配置 Ant Design Vue 的全局语言为中文（通过 a-config-provider），并使用 Vue Router 渲染当前路由匹配的组件。在样式上，设置了全局的字体和高度。-->