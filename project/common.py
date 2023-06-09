import jwt

from datetime import datetime
from datetime import timedelta

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordBearer

from .database import User

SECRET_KEY = 'PruebaToken2023'

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/auth')

def create_access_token(user, days=7):
    data = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(days=days)
    }

    return jwt.encode(data, SECRET_KEY, algorithm="HS256")


def decode_access_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except Exception as err:
        return None


def get_current_user(token: str = Depends(oauth2_schema)):
    data = decode_access_token(token)

    if data:
        return User.select().where(User.id == data['user_id']).first()
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Access token no valido',
            headers={ 'WWW-Autenticate': 'Bearer' }
        )