import aioredis

async def get_redis():
    redis = aioredis.from_url("redis://localhost:6379")
    return redis