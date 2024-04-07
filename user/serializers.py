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
        name = validated_data.pop('username', None)

        if name is None:
            raise exceptions.APIException('Username is required')

        splitname = name.replace(" ", "")

        if get_user_model().objects.filter(username=splitname).exists():
            raise exceptions.APIException('Username is exists')

        return get_user_model().objects.create_user(username=splitname, **validated_data)