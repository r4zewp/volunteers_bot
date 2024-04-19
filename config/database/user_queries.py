import asyncpg

async def get_user(conn, id):
    query = f"SELECT username FROM public.user WHERE telegram_user_id = $1;"
    row = await conn.fetchrow(query, id)

    if row:
        return {
            "user": {
                "username": row['username']
            }
        }
    else:
        return None
    