from dotenv import load_dotenv
load_dotenv()

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