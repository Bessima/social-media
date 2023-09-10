from aioredis import Redis, from_url


class RedisApiClient:
    _session: Redis

    def __init__(self, url: str):
        self._session = from_url(url, encoding="utf-8", decode_responses=True)

    async def add(self, name, data: dict):
        await self._session.xadd(name, data, maxlen=1000)

    async def get(self, key, count=100) -> list[set]:
        return await self._session.xrange(key, '-', '+', count)

    async def close(self):
        await self._session.close()
