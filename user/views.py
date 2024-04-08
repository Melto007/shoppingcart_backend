from rest_framework import (
    generics,
    mixins,
    status
)
from rest_framework.response import Response
from .serializers import (
    UserSerializer
)
from django.contrib.auth import get_user_model

"""
    method: POST
    description: post - create a user
    params: username, email, phone number, password
"""
class UserViewset(
    mixins.ListModelMixin,
    generics.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def create(self, request):
        try:
            data = request.data

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            response = {
                'data': 'user created successfully',
                'status': status.HTTP_200_OK
            }

            return Response(response)
        except Exception as e:
            response = {
                'data': e.args,
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(response)

"""
    method: POST
    params: email, password
    description: post - login user
"""
class LoginViewSet(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def create(self, request):
        pass
