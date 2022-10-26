from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewset, GroupViewset


router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'groups', GroupViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
