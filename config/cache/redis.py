from redis import asyncio as aioredis
from dotenv import load_dotenv
import os

load_dotenv()

redis_url = os.getenv('REDIS_URL')

async def get_redis():
    redis = aioredis.from_url(redis_url)
    return redis

async def get_cached_user(telegram_id):
    user_key = "user_id_" + str(telegram_id)
    
    redis = await get_redis()
    user = redis.get(user_key)
    
    if (user):
        await redis.close()
        return user.decode('utf-8')
    
    else:
        await redis.close()
        return None

async def set_user_cache(telegram_id):
    user_key = "user_id_" + str(telegram_id)
    
    redis = await get_redis()
    await redis.setex(user_key, 9999, telegram_id)
    
    user_cached = await redis.get(user_key)
    return user_cached.decode('utf-8')