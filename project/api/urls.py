from django.urls import path, include

from rest_framework import routers
from project.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('api/', include(router.urls)),
]
