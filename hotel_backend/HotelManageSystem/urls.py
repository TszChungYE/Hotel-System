from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from HotelManageSystem import settings

# 主路由
urlpatterns = [
                  path('admin/', admin.site.urls),  # 后台管理系统
                  path('hotel/', include('hotel.urls')),  # 酒店管理系统
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 媒体文件路径
