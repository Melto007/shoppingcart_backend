from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewset,
    LoginViewSet
)

router = DefaultRouter()

router.register('user', UserViewset, basename='user')
router.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls))
]
