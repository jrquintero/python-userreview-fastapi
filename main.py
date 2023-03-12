from fastapi import FastAPI
from database import User
from database import Movie
from database import UserReview
from database import database as connection

from schemas import UserBaseModel

app = FastAPI(title='Poyecto para reseñar peliculas',
            descripcion='En este proyecto seremos capacer de desplegar peliculas',
            version=1)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    
    connection.create_tables([User, Movie, UserReview])
    print('Connecting...')

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
    
    print('Close')

@app.get('/')
async def index():
    return 'Hola mundo, desde un servidor en FastAPI'


@app.post('/users')
async def create_user(user: UserBaseModel):
    user = User.create(
        username=user.username,
        password=user.password
    )

    return user.id


@app.get('/about')
async def about():
    return 'About'