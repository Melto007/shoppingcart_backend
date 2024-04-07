from rest_framework import (
    viewsets,
    mixins,
    status
)
from rest_framework.response import Response

"""
    method: POST
    description: post - create a user
    params: username, email, phone number, password
"""
class UserViewset(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    def create(self, request):
        try:
            data = request.data

            response = {
                'data': data,
                'status': status.HTTP_200_OK
            }

            return Response(response)
        except Exception as e:
            response = {
                'data': e.args,
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(response)

    def list(self, request):
        return Response('success')