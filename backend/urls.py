from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from Authentication import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'users', views.UserViewSet)
router_v1.register(r'accounts', views.UserAccountViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include(router_v1.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
