import asyncpg
from models import User
from models import Volunteer
from user_queries import get_user_by_id
from database import objects

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
