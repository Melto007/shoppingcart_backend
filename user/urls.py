from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewset,
    LoginViewSet,
    RefreshViewset,
    ProfileViewset
)

router = DefaultRouter()

router.register('user', UserViewset, basename='user')
router.register('login', LoginViewSet, basename='login')
router.register('refresh', RefreshViewset, basename='refresh')
router.register('profile', ProfileViewset, basename='profile')

urlpatterns = [
    path('', include(router.urls))
]
