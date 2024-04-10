from rest_framework import (
    viewsets,
    mixins,
    status,
    exceptions
)
from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    TokenSerializer,
    ProfileSerializer
)
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from utils.authentication import (
    create_access_token,
    create_refresh_token,
    refresh_decode_token,
    JWTAuthentication
)
from core.models import (
    TokenUser
)
import datetime

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

            TokenUser.objects.create(user=queryset.id, token=refresh_token)

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

"""
    method: POST
    description: Refresh token
"""
class RefreshViewset(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = TokenSerializer
    queryset = TokenUser.objects.all()

    def create(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token', False)
            print(refresh_token)

            id = refresh_decode_token(refresh_token)

            if not self.queryset.filter(
                user=id,
                token=refresh_token,
                expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
            ).exists():
                self.queryset.filter(
                    user=id,
                    token=refresh_token,
                    expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
                ).delete()
                raise exceptions.AuthenticationFailed('Unauthorized User')

            access_token = create_access_token(id)

            datas = {
                'access_token': access_token
            }

            response = {
                'data': datas,
                'status': status.HTTP_200_OK
            }

            return Response(response)
        except Exception as e:
            response = {
                'data': e.args,
                'status': status.HTTP_404_NOT_FOUND
            }
            return Response(response)

"""
    method: List
    description: View profile user
"""
class ProfileViewset(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    authentication_classes = [JWTAuthentication]
    serializer_class = ProfileSerializer
    queryset = get_user_model().objects.all()

    def list(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(email=request.user)
            serializer = self.get_serializer(instance, many=False)

            response = {
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
            return Response(response)
        except Exception as e:
            response = {
                'data': e.args,
                'status': status.HTTP_404_NOT_FOUND
            }
            return Response(response)