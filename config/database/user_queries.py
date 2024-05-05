import asyncpg
from models import User
from models import Volunteer

# async def get_user(conn, id):
#     query = f"SELECT username FROM public.user WHERE telegram_user_id = $1;"
#     row = await conn.fetchrow(query, id)

#     if row:
#         return {
#             "user": {
#                 "username": row['username']
#             }
#         }
#     else:
#         return None

# async def create_user(conn, phone_num, username, tg_id):

#     query = """
#     INSERT INTO public.user (phone_number, username, telegram_user_id)
#     VALUES ($1, $2, $3)
#     RETURNING id
#     """
    
#     user_id = await conn.fetch(query, phone_num, username, tg_id)
    
#     await conn.close()

#     return user_id

async def add_user(username, phone_number, telegram_id):
    try:
        # Создание нового пользователя и сохранение его в базе данных
        user = await User.create(username=username, phone_number=phone_number, telegram_id=telegram_id)
        return user
    except Exception as e:
        return None

async def get_user_by_id(user_id):
    try:
        # Поиск пользователя по ID
        user = await User.get(User.id == user_id)
        return user
    except User.DoesNotExist:
        return None
    except Exception as e:
        return None


async def create_volunteer(uid, vol_info:dict):
    
    user = get_user_by_id(uid)

    if (user != None):

        volunteer = await 

        return
    
    else: return None
