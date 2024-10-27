from django.urls import path

from hotel import views

# 子路由
app_name = 'hotel'
urlpatterns = [
    # ---------------------------后台管理员api-------------------------------
    path('admin/thing/list', views.admin.thing.list_api),  # 房间列表
    path('admin/thing/detail', views.admin.thing.detail),  # 房间详情
    path('admin/thing/create', views.admin.thing.create),  # 新建房间
    path('admin/thing/update', views.admin.thing.update),  # 更新房间
    path('admin/thing/delete', views.admin.thing.delete),  # 删除房间

    path('admin/classification/list', views.admin.classification.list_api),  # 分类列表
    path('admin/classification/create', views.admin.classification.create),  # 添加分类
    path('admin/classification/update', views.admin.classification.update),  # 更新分类
    path('admin/classification/delete', views.admin.classification.delete),  # 删除分类
    path('admin/tag/list', views.admin.tag.list_api),  # 标签列表
    path('admin/tag/create', views.admin.tag.create),  # 创建标签
    path('admin/tag/update', views.admin.tag.update),  # 修改标签
    path('admin/tag/delete', views.admin.tag.delete),  # 删除标签

    path('admin/order/list', views.admin.order.list_api),  # 订单列表
    path('admin/order/create', views.admin.order.create),  # 创建订单
    path('admin/order/update', views.admin.order.update),  # 修改订单
    path('admin/order/cancel_order', views.admin.order.cancel_order),  # 取消订单
    path('admin/order/delete', views.admin.order.delete),  # 删除订单
    path('admin/order/ok_order', views.admin.order.ok_order),  # 完成订单

    path('admin/loginLog/list', views.admin.loginLog.list_api),  # 登录日志列表
    path('admin/loginLog/create', views.admin.loginLog.create),  # 创建登录日志
    path('admin/loginLog/update', views.admin.loginLog.update),  # 修改登录日志
    path('admin/loginLog/delete', views.admin.loginLog.delete),  # 删除登录日志

    path('admin/user/list', views.admin.user.list_api),  # 用户列表
    path('admin/user/create', views.admin.user.create),  # 创建用户
    path('admin/user/update', views.admin.user.update),  # 修改用户
    path('admin/user/updatePwd', views.admin.user.updatePwd),  # 修改密码
    path('admin/user/delete', views.admin.user.delete),  # 删除用户
    path('admin/user/info', views.admin.user.info),  # 用户信息
    path('admin/adminLogin', views.admin.user.admin_login),  # 管理员登录

    # ----------------------------前台用户api-------------------------------------------
    path('index/classification/list', views.index.classification.list_api),  # 分类列表
    path('index/user/login', views.index.user.login),  # 用户登录
    path('index/thing/list', views.index.thing.list_api),  # 房间列表
    path('index/thing/detail', views.index.thing.detail),  # 房间详情

]
