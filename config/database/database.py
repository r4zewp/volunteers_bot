import os
from dotenv import load_dotenv
import asyncpg

load_dotenv()

pg_user = os.getenv('PG_USER')
pg_pw = os.getenv('PG_PASSWORD')
pg_db = os.getenv('PG_DATABASE')

async def create_pool():
    return await asyncpg.create_pool(
        user=pg_user,
        password=pg_pw,
        database=pg_db,
        host='localhost'
    )

