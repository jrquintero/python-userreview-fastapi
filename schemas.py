from pydantic import BaseModel
from pydantic import validator

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