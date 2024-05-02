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

async def create_user(conn, phone_num, username, tg_id):

    query = """
    INSERT INTO users (phone_number, username, telegram_user_id)
    VALUES ($1, $2, $3);
    RETURNING id;
    """
    
    user_id = await conn.fetchval(query, phone_num, username, tg_id)
    
    await conn.close()

    return user_id


async def create_volunteer(conn, uid, vol_info:dict):
    
    user = get_user(conn, id)

    if (user):

        query = """
        INSERT INTO volunteers (user_id, name, surename, middlename, education_type, education_program, course_number)
        VALUES ($1, $2, $3, $4, $5, $6, $7)
        RETURNING v_id
        """
        volunteer_id = await conn.fetchval(query, uid, vol_info['name'], vol_info['surename'],
                            vol_info['middlename'], vol_info['education_type'], vol_info['education_program'],
                            vol_info['course_number'])
        await conn.close()

        return volunteer_id
    
    else: return None
