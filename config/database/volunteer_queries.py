import asyncpg
from config.models.User import User
from config.models.Volunteer import Volunteer
from config.database.user_queries import get_user_by_id
from config.database.database import objects

async def create_volunteer(uid, vol_info: dict):
    user = await get_user_by_id(uid)

    if user is not None:
        volunteer = await objects.create(
            Volunteer,
            user=user,
            name=vol_info['name'],
            surename=vol_info['surename'],
            middlename=vol_info['middlename'],
            education_type=vol_info['education_type'],
            education_programm=vol_info['education_program'],
            course_number=vol_info['course_number'],
        )
        return volunteer
    else:
        return None

# Асинхронная функция для получения волонтера по ID
async def get_volunteer_by_id(v_id):
    try:
        volunteer = await objects.get(Volunteer, Volunteer.v_id == v_id)
        return volunteer
    except Volunteer.DoesNotExist:
        print("Volunteer does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Асинхронная функция для получения всех волонтеров
async def get_all_volunteers():
    try:
        volunteers = await objects.execute(Volunteer.select())
        return volunteers
    except Exception as e:
        print(f"Error: {e}")
        return None


# Асинхронная функция для получения волонтера по ID пользователя
async def get_volunteer_by_user_id(user_id) -> Volunteer:
    try:
        user = await objects.get(User, User.id == user_id)
        volunteer = await objects.get(Volunteer, Volunteer.user == user)
        # Выводим все поля волонтера для проверки
        print(f"VOLUNTEER**** ID: {volunteer.v_id}, Name: {volunteer.name}, Surname: {volunteer.surename}, Middlename: {volunteer.middlename}, Education Type: {volunteer.education_type}, Education Program: {volunteer.education_programm}, Course Number: {volunteer.course_number}")
        return volunteer
    except User.DoesNotExist:
        print("User does not exist.")
        return None
    except Volunteer.DoesNotExist:
        print("Volunteer does not exist.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None