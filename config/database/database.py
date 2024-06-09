import os
from dotenv import load_dotenv
import asyncpg
from peewee import PostgresqlDatabase
import peewee_async

load_dotenv()

pg_user = os.getenv('PG_USER')
pg_pw = os.getenv('PG_PASSWORD')
pg_db = os.getenv('PG_DATABASE')

async def create_pool():
    db = await peewee_async.PostgresqlDatabase(
        'postgres',
        user=pg_user,
        password=pg_pw,
        host='167.172.99.57',
        port=5432
    )
    objects = peewee_async.Manager(db)
    return objects
db = PostgresqlDatabase(
    'postgres',
    user=pg_user,
    password=pg_pw,
    host='167.172.99.57',
    port=5432
)
objects = peewee_async.Manager(db)

async def create_pool():
    return db, objects

