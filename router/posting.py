from custom_exception.handler_exceptions import CuztomException, PostException
from fastapi import APIRouter

routes = APIRouter()


@routes.get("/exception")
def exc():
    raise CuztomException(status_code=400, detail="this is cuztom exception")


@routes.get("/poEx")
def posting_custom_errors():
    raise PostException(
        status_code=200,
        detail="This is lucky one!No need to try again!!!!!!",
    )
