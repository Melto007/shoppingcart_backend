from dotenv import load_dotenv
load_dotenv()

from rest_framework import exceptions
import jwt
import datetime
import os

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