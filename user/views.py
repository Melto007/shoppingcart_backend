from rest_framework import (
    viewsets,
    mixins,
    status,
    exceptions
)
from rest_framework.response import Response
from .serializers import (
    UserSerializer
)
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from utils.authentication import (
    create_access_token,
    create_refresh_token
)

"""
    method: POST
    description: post - create a user
    params: username, email, phone number, password
"""
class UserViewset(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
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
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def create(self, request):
        try:
            data = request.data
            email = data.get('email', None)
            password = data.get('password', None)

            queryset = get_object_or_404(self.queryset, email=email)

            if not queryset:
                raise exceptions.AuthenticationFailed('Invalid credential')

            if not queryset.check_password(password):
                raise exceptions.AuthenticationFailed('Invalid credential')

            access_token = create_access_token(queryset.id)
            refresh_token = create_refresh_token(queryset.id)

            response = Response()

            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True
            )

            datas = {
                'access_token': access_token,
            }

            response.data = {
                'data': datas,
                'status': status.HTTP_200_OK
            }
            return response
        except Exception as e:
            response = {
                'data': e.args,
                'status': status.HTTP_404_NOT_FOUND
            }
            return Response(response)