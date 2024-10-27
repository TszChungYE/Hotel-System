<template>
  <a-layout id="components-layout-demo-custom-trigger">
    <a-layout-header style="background: green; padding: 0">
      <div class="header">
        <img class="header-logo" :src="logo">
        <span class="header-title" style="color: white;">学人馆 后台管理系统</span>
        <div class="empty"></div>
        <a-button style="margin-right: 500px;" @click="handlePreview">进入前台预定系统查看</a-button>
        <span>管理员[{{ userStore.admin_user_name }}]</span>
        <a class="header-quit" @click="handleLogout">退出</a>
      </div>
    </a-layout-header>
    <a-layout>
      <a-layout-sider v-model="collapsed" collapsible :style="{ background: 'white' }" >
        <a-menu style="overflow:auto; overflow-x: hidden;" v-model:selectedKeys="selectedKeys" theme="dark" mode="inline" @click="handleClick">

          <a-menu-item key="user">
            <user-outlined/>
            <span>用户管理</span>
           </a-menu-item>

          <a-menu-item key="order">
            <dollar-outlined/>
            <span>订单管理</span>
          </a-menu-item>


          <a-sub-menu>
            <template #icon>
              <folder-outlined/>
            </template>
            <template #title>酒店管理</template>

            <a-menu-item key="thing">
              <database-outlined/>
              <span>客房管理</span>
            </a-menu-item>

            <a-menu-item key="classification">
              <layout-outlined/>
              <span>房型管理</span>
            </a-menu-item>

            <a-menu-item key="tag">
              <tag-outlined/>
              <span>标签管理</span>
            </a-menu-item>
            <!--          把房间标签换成房间配件-->

          </a-sub-menu>

          <a-menu-item key="loginLog">
            <appstore-outlined/>
            <span>登录日志</span>
          </a-menu-item>



        </a-menu>
      </a-layout-sider>
      <a-layout-content :style="{ margin: '16px 16px', minHeight: '200px' }">
        <router-view/>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>


<script setup lang="ts">
import {useRouter, useRoute} from 'vue-router'
import logo from '/@/assets/images/sysu.png'

import {
  AppstoreOutlined,
  FolderOutlined,
  UserOutlined,
  TagOutlined,
  DollarOutlined,
  LayoutOutlined,
  DatabaseOutlined
} from '@ant-design/icons-vue';

import {ref} from 'vue';
import {useUserStore} from "/@/store";

const userStore = useUserStore();

const selectedKeys = ref<any[]>([])
const collapsed = ref<boolean>(false)

const router = useRouter()
const route = useRoute()

const handleClick = ({item, key, keyPath}) => {
  console.log('点击路由===>', key)
  router.push({
    name: key,
  })
}

const handlePreview = ()=>{
  let text = router.resolve({name: 'index'})
  window.open(text.href, '_blank')
}

onMounted(() => {
  console.log('当前路由===>', route.name)
  selectedKeys.value = [route.name]
})


const handleLogout = () => {
  userStore.adminLogout().then(res => {
    router.push({name: 'adminLogin'})
  })
}

</script>
<style scoped lang="less">

// header样式
.header {
  display: flex;
  flex-direction: row;
  align-items: center; // 垂直居中
  padding-left: 24px;
  padding-right: 24px;

  .header-logo {
    width: 32px;
    height: 32px;
    cursor: pointer;
  }

  .header-title {
    margin-left: 16px;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
  }

  .empty {
    flex: 1;
  }

  .header-quit {
    margin-left: 12px;
  }
}


#components-layout-demo-custom-trigger {
  height: 100%;
}

#components-layout-demo-custom-trigger .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: green;
}


:deep(.ant-layout-content) {
  overflow-x: hidden;
}

:deep(.ant-layout-sider) {
  padding: 16px 0;
  background-color: #f0f2f5;
}

:deep(.ant-menu) {
  padding-top: 16px;
  height: 100%;
}

//:deep(.ant-layout-sider-trigger) {
//  background-color: #fff;
//  height: 10px; // 设置0 隐藏
//}
</style>
