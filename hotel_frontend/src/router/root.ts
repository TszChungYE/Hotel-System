// 路由表
const constantRouterMap = [
  // ************* 前台路由 **************
  {
    path: '/',
    redirect: '/index'
  },
  {
    path: '/index',
    name: 'index',
    redirect: '/index/portal',
    component: () => import('/@/views/index/index.vue'),
    children: [
      {
        path: 'login',
        name: 'login',
        component: () => import('/@/views/index/login.vue')
      },
      {
        path: 'portal',
        name: 'portal',
        component: () => import('/@/views/index/portal.vue')
      },
      {
        path: 'detail',
        name: 'detail',
        component: () => import('/@/views/index/detail.vue')
      },
      {
        path: 'confirm',
        name: 'confirm',
        component: () => import('/@/views/index/confirm 2.vue')
      }
    ]
  },
  {
    path: '/adminLogin',
    name: 'adminLogin',
    component: () => import('/@/views/admin/admin-login.vue'),
  },
  {
    path: '/admin',
    name: 'admin',
    redirect: '/admin/thing',
    component: () => import('/@/views/admin/main.vue'),
    children: [
      { path: 'order', name: 'order', component: () => import('/@/views/admin/order.vue') },
      { path: 'thing', name: 'thing', component: () => import('/@/views/admin/thing.vue') },
      { path: 'user', name: 'user', component: () => import('/@/views/admin/user.vue') },
      { path: 'classification', name: 'classification', component: () => import('/@/views/admin/classification.vue') },
      { path: 'tag', name: 'tag', component: () => import('/@/views/admin/tag.vue') },
      { path: 'loginLog', name: 'loginLog', component: () => import('/@/views/admin/login-log.vue') }
    ]
  },
];
export default constantRouterMap;
