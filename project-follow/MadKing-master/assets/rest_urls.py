#_*_coding:utf-8_*_
__author__ = 'jieli'
from django.conf.urls import url, include
from rest_framework import routers
from assets import rest_views as views
from assets import views as asset_views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'assets', views.AssetViewSet)
router.register(r'servers', views.ServerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),         #方法1 ，完全使用restful提供的接口进行设计；
    url(r'asset_list/$',views.AssetList ),   #方法2：只使用restful的序列化的方法和response方法来进行实现
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^dashboard_data/',asset_views.get_dashboard_data,name="get_dashboard_data")
]

#两种方法的验证：
# 方法2 通过访问 url: http://localhost:9000/api/asset_list/
#方法1：通过方法 url http://localhost:9000/api/assets/
#上面两个url获取的数据完全一样；只是采用了两种不同的实现方法；