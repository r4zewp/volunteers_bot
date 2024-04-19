from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profile=KeyboardButton(text='Профиль')
projects=KeyboardButton(text='Проекты')
grades=KeyboardButton(text='Табель')

start_markup_logged=ReplyKeyboardMarkup(keyboard=[[profile, projects, grades]])