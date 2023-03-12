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

class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, usernanme):
        if len(usernanme) < 3 or len(usernanme) > 50:
            raise ValueError('La longitud del nombre de usuario debe encontrarse entre 3 y 50 caracteres')
        
        return usernanme

class UserResponseModel(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict