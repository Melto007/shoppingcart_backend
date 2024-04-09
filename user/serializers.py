from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from core.models import TokenUser

"""
    description: serializer for create user
"""
class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'phone_number', 'company_name']
        extra_kwargs = {'password': { 'write_only': True }}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

"""
    description: serializer for token user
"""
class TokenSerializer(ModelSerializer):
    class Meta:
        model = TokenUser
        fields = ['id', 'token', 'expired_at']

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'phone_number', 'company_name']