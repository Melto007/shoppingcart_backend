from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions

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