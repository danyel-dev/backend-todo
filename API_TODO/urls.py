from email.mime import base
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewset, GroupViewset
from core.views import ListViewset, ItemViewset


router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'groups', GroupViewset)
router.register(r'list', ListViewset, basename='list')
router.register(r'item', ItemViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
