import uvicorn
from core import init_db
from fastapi import FastAPI
from starlette.responses import HTMLResponse

from social_media.api import api_router
from social_media.core.middlewares import AppExceptionMiddleware

app = FastAPI()

app.include_router(api_router)

app.add_middleware(AppExceptionMiddleware)


@app.get("/")
async def main_route():
    return HTMLResponse("Hi, go to <a href='/docs'>Swagger Docs</a>")


@app.on_event("startup")
async def startup():
    await init_db()


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
