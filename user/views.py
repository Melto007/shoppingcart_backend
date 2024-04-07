from rest_framework import (
    viewsets,
    mixins
)
from rest_framework.response import Response

"""
    create a user
"""
class UserViewset(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    def list(self, request):
        return Response('success')