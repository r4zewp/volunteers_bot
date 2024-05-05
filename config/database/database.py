import os
from dotenv import load_dotenv
import asyncpg
from peewee import PostgresqlDatabase


load_dotenv()

pg_user = os.getenv('PG_USER')
pg_pw = os.getenv('PG_PASSWORD')
pg_db = os.getenv('PG_DATABASE')

# db = await PostgresqlDatabase('postgres@2.tcp.eu.ngrok.io', user=pg_user, password=pg_pw, host='2.tcp.eu.ngrok.io', port='17785')

async def create_pool():
    return await PostgresqlDatabase(
        'postgres@2.tcp.eu.ngrok.io',
        user=pg_user,
        password=pg_pw,
        host='2.tcp.eu.ngrok.io',
        port='17785'
    )


# async def create_pool():
#     return await asyncpg.create_pool(
#         user=pg_user,
#         password=pg_pw,
#         database=pg_db,
#         host='localhost'
#     )

