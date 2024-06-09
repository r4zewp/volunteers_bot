from config.models.User import User
from config.models.Volunteer import Volunteer
from peewee_async import Manager

# Асинхронная функция для добавления пользователя
async def add_user(username, phone_number, telegram_id):
    try:
        # Создание нового пользователя и сохранение его в базе данных
        user = await objects.create(User, username=username, phone_number=phone_number, telegram_user_id=telegram_id)
        return user
    except Exception as e:
        print(f"Error: {e}")
        return None

# Асинхронная функция для получения пользователя по ID
async def get_user_by_id(user_id, objects: Manager):
    try:
        user = await objects.get(User, User.telegram_user_id == user_id)
        print("USER**** ", user)
        return user
    except User.DoesNotExist:
        print("User does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None