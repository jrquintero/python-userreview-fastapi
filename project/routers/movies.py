from fastapi import APIRouter
from fastapi import HTTPException

from ..database import Movie

from ..schemas import MovieRequestModel
from ..schemas import MovieResponseModel

router = APIRouter(prefix='/movies')

@router.post('', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):

    movie = Movie.create(
        title=movie.title
    )

    return movie
