from social_media.clients.redis import RedisApiClient
from social_media.core.settings import config


async def get_redis() -> RedisApiClient:
    return RedisApiClient(url=config.REDIS_URL)
