import pydantic


class AppSettings(pydantic.BaseSettings):
    JWT_SECRET: str
    JWT_ALGORITHM: str

    DATABASE_URL: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = AppSettings()
