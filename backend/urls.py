from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from Authentication import views as AuthViews
from Topics import views as TopicViews

router_v1 = routers.DefaultRouter()
router_v1.register(r'users', AuthViews.UserViewSet)
router_v1.register(r'accounts', AuthViews.UserAccountViewSet)
router_v1.register(r'new', TopicViews.NewViewSet, base_name="new")
router_v1.register(r'feed', TopicViews.FeedViewSet, base_name="feed")
router_v1.register(r'topic/subscriptions',
                   TopicViews.TopicSubscription,
                   base_name="subscriptions")
router_v1.register(r'topic', TopicViews.TopicViewSet, base_name="topic")


urlpatterns = [
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/register', AuthViews.UserAccountRegistration.as_view()),
    url(r'^v1/login', obtain_auth_token, name='auth-token'),
    url(r'^v1/', include(router_v1.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^django-rq/', include('django_rq.urls'))
]
