from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def create_profile_kb():

    edit = KeyboardButton(text="Изменить")
    projects = KeyboardButton(text="Мои проекты")

    return ReplyKeyboardMarkup(keyboard=[[edit, projects]])