from fastapi import FastAPI

from .database import User
from .database import Movie
from .database import UserReview

from .routers import user_router
from .routers import movie_router
from .routers import review_router

from .database import database as connection

app = FastAPI(title='Poyecto para reseñar peliculas',
            descripcion='En este proyecto seremos capacer de desplegar peliculas',
            version=1)

app.include_router(user_router)
app.include_router(movie_router)
app.include_router(review_router)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    
    connection.create_tables([User, Movie, UserReview])
    # print('Connecting...')

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
    
    print('Close')

@app.get('/')
async def index():
    return 'Hola mundo, desde un servidor en FastAPI'


@app.get('/about')
async def about():
    return 'About'