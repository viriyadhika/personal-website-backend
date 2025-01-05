from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from app.env import ALLOWED_ORIGIN
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOWED_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": f"{exc.errors()}", "errors": exc.errors()},
    )


from app.crawler import crawler_router

app.include_router(crawler_router)

from app.auth import auth_router

app.include_router(auth_router)

from app.flashcard import flashcard_router

app.include_router(flashcard_router)
