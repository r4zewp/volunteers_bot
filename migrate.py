# migrate.py
import os
from dotenv import load_dotenv
from peewee import PostgresqlDatabase
from peewee_migrate import Router
import sys
import peewee_async
import peewee

load_dotenv()

pg_user = os.getenv('PG_USER')
pg_pw = os.getenv('PG_PASSWORD')
pg_db = os.getenv('PG_DATABASE')
sv_host = os.getenv('SV_HOST')
pg_port = os.getenv('PG_PORT')

# Define your database connection
db = peewee.PostgresqlDatabase(
    'postgres',
    user=pg_user,
    password=pg_pw,
    host=sv_host,
    port=pg_port
)

# Initialize the migration router
router = Router(db, migrate_dir='migrations')

if __name__ == "__main__":
    command = sys.argv[1]
    if command == 'create':
        router.create(name=sys.argv[2], auto=sys.argv[3:])
    elif command == 'migrate':
        router.run()
    else:
        print(f"Unknown command: {command}")
