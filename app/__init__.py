from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from app.env import ALLOWED_ORIGIN
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Request
from app.crawler import crawler_router, init_crawler
from app.auth import auth_router
from app.flashcard import flashcard_router
from app.todo import todo_router

from contextlib import asynccontextmanager

from app.common.scheduler import scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    close_crawler = init_crawler()
    scheduler.start()
    yield
    scheduler.shutdown()
    close_crawler()


app = FastAPI(lifespan=lifespan)

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


app.include_router(crawler_router)

app.include_router(auth_router)

app.include_router(flashcard_router)

app.include_router(todo_router)
