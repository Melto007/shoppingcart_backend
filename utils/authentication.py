from dotenv import load_dotenv
load_dotenv()

from rest_framework import exceptions
import jwt
import datetime
import os
from rest_framework.authentication import (
    BaseAuthentication,
    get_authorization_header
)
from django.contrib.auth import get_user_model

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = get_user_model().objects.get(pk=id)

            return { user, None }
        raise exceptions.AuthenticationFailed('Unauthorized User')

""" create access token for login user """
def create_access_token(id):
    secret = os.environ['ACCESS_TOKEN']
    payload = jwt.encode(
        {
            'id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            'iat': datetime.datetime.utcnow()
        },
        secret,
        algorithm='HS256'
    )
    return payload

def decode_access_token(token):
    try:
        secret = os.environ['ACCESS_TOKEN']
        payload = jwt.decode(
            token,
            secret,
            algorithms=['HS256']
        )
        return payload['id']
    except:
        raise exceptions.AuthenticationFailed('Invalid credential')

""" create refresh token for login user """
def create_refresh_token(id):
    secret = os.environ['REFERESH_SECRET']
    payload = jwt.encode(
        {
            'id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5),
            'iat': datetime.datetime.utcnow()
        },
        secret,
        algorithm='HS256'
    )
    return payload

""" refresh decode token """
def refresh_decode_token(token):
    try:
        secret = os.environ['REFERESH_SECRET']
        payload = jwt.decode(
            token,
            secret,
            algorithms=['HS256']
        )
        return payload['id']
    except:
        raise exceptions.AuthenticationFailed('Invalid credential')