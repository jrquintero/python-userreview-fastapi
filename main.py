from fastapi import FastAPI
from fastapi import HTTPException

from database import User
from database import Movie
from database import UserReview
from database import database as connection

from schemas import UserRequestModel
from schemas import UserResponseModel
from schemas import ReviewRequestModel
from schemas import ReviewResponseModel
from schemas import MovieRequestModel
from schemas import MovieResponseModel

app = FastAPI(title='Poyecto para reseñar peliculas',
            descripcion='En este proyecto seremos capacer de desplegar peliculas',
            version=1)

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


@app.post('/users', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'El usuario ya se encuentra registrado')

    hash_password = User.create_password(user.password)

    user = User.create(
        username=user.username,
        password=hash_password
    )

    return user


@app.post('/movies', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):

    movie = Movie.create(
        title=movie.title
    )

    return movie


@app.post('/reviews', response_model=ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel):
    
    user_review = UserReview.create(
        user_id=user_review.user_id,
        movie_id=user_review.movie_id,
        review=user_review.review,
        score=user_review.score
    )

    return user_review


@app.get('/about')
async def about():
    return 'About'