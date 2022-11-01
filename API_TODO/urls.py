from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewset, GroupViewset
from core.views import ListViewset, ItemViewset
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'groups', GroupViewset)
router.register(r'list', ListViewset, basename='list')
router.register(r'item', ItemViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),
    path('admin/', admin.site.urls),
]
