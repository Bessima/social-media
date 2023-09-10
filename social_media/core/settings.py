import pydantic

# class RedisSettings(pydantic.BaseSettings):
#     URL: str
#
#     class Config:
#         env_file = '.env'
#         env_file_encoding = 'utf-8'


class AppSettings(pydantic.BaseSettings):
    # redis: RedisSettings

    JWT_SECRET: str
    JWT_ALGORITHM: str

    DATABASE_URL: str
    DATABASE_READ_URL: str

    REDIS_URL: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    # @classmethod
    # def create(cls):
    #     return AppSettings(
    #         redis=RedisSettings()
    #     )


config = AppSettings()
