from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewset,
    LoginViewSet,
    RefreshViewset
)

router = DefaultRouter()

router.register('user', UserViewset, basename='user')
router.register('login', LoginViewSet, basename='login')
router.register('refresh', RefreshViewset, basename='refresh')

urlpatterns = [
    path('', include(router.urls))
]
