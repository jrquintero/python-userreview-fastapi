from typing import Any

from pydantic import BaseModel
from pydantic import validator

from peewee import ModelSelect

from pydantic.utils import GetterDict

"""
Esta Clase solo serializa o convierte modelos de Peewee
"""
class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):

        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        
        return res

class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


# ------------- User --------------

class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, usernanme):
        if len(usernanme) < 3 or len(usernanme) > 50:
            raise ValueError('La longitud del nombre de usuario debe encontrarse entre 3 y 50 caracteres')
        
        return usernanme

class UserResponseModel(ResponseModel):
    id: int
    username: str


# ------------- Review --------------

class ReviewRequestModel(BaseModel):
    user_id: int
    movie_id: int
    review: str
    score: int

    @validator('score')
    def score_validator(cls, score):

        if score < 1 or score > 5:
            raise ValueError('El rango para el score es de 1 a 5')
        
        return score

class ReviewResponseModel(ResponseModel):
    id: int
    movie_id: int
    review: str
    score: int


# ------------- Movie --------------

class MovieRequestModel(BaseModel):
    title: str

class MovieResponseModel(ResponseModel):
    id: int
    title: str
