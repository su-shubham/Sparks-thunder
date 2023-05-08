from fastapi import FastAPI
from router.posting import routes
from custom_exception.handler_exceptions import CuztomException, PostException
from fastapi import Request
from fastapi.responses import JSONResponse
from background_tasks import log_email

app = FastAPI()

app.include_router(routes, prefix="/api")
app.include_router(log_email.router, prefix="/log")


@app.exception_handler(CuztomException)
def cuztom_exception(req: Request, cus: CuztomException):
    return JSONResponse(
        status_code=cus.status_code,
        content={"message": f"error{cus.detail}"},
    )


@app.exception_handler(PostException)
def post_exception(req: Request, postEx: PostException):
    return JSONResponse(
        status_code=postEx.status_code,
        content={"message": f"{postEx.detail}"},
    )
