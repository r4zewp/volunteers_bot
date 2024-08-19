from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import *

def create_admin_kb():
    projects = KeyboardButton(text='Все проекты')
    volunteers = KeyboardButton(text='Все волонтеры')
    add_new_project = KeyboardButton(text='Создать проект')

    markup = ReplyKeyboardMarkup(keyboard=[[add_new_project, projects], [volunteers]])
    return markup