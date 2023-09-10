from os import environ, path

import databases
from dotenv import load_dotenv
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
load_dotenv(path.join(BASE_DIR, ".env"))

DATABASE_URL = str(environ.get('DATABASE_URL', ''))
DATABASE_READ_URL = str(environ.get('DATABASE_READ_URL', ''))

# databases query builder
database = databases.Database(DATABASE_URL)
database_read = databases.Database(DATABASE_READ_URL)

engine = create_async_engine(DATABASE_URL)
# engine_read = create_async_engine(DATABASE_READ_URL)

metadata = MetaData()

Base = declarative_base()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # async with engine_read.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


async def get_read_session() -> AsyncSession:
    pass
    # async_session = sessionmaker(engine_read, class_=AsyncSession, expire_on_commit=False)
    # async with async_session() as session:
    #     yield session
