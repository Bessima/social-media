from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from social_media.exceptions import AppException


class AppExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response = await call_next(request)
        except AppException as exception:
            return JSONResponse(
                status_code=exception.status,
                content={"message": exception.message},
            )

        return response
