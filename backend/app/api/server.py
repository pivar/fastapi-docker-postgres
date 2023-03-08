from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from app.utils.exception_handlers import request_validation_exception_handler, http_exception_handler, \
    unhandled_exception_handler
from app.middleware import log_request_middleware

appKalya = FastAPI(title="KalyaApp", description="Kalya API", version="0.0.1")


def get_application():
    appKalya.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    """
    Custom middleware for exception handling and logging
    """
    appKalya.middleware("http")(log_request_middleware)
    appKalya.add_exception_handler(RequestValidationError, request_validation_exception_handler)
    appKalya.add_exception_handler(HTTPException, http_exception_handler)
    appKalya.add_exception_handler(Exception, unhandled_exception_handler)
    return appKalya


app = get_application()


@app.get('/')
def index():
    return {'data': {'details': {'hello FastAPI details'}}}


@app.get('/lumba/{numb}')
def lumbacheck(numb: int):
    return {'data': {'msg': 'no lumba here man', 'id': numb}}
