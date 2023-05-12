import uvicorn
from core import init_db
from fastapi import FastAPI

from social_media.api import api_router

app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def main_route():
    return {"message": "Hi"}


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
