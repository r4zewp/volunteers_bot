from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_markup_logged():
    
    profile=KeyboardButton(text='Профиль')
    projects=KeyboardButton(text='Проекты')
    grades=KeyboardButton(text='Табель')
    
    markup=ReplyKeyboardMarkup(keyboard=[[profile, projects], [grades]], 
                               resize_keyboard=True, 
                               input_field_placeholder="ASD")

    return markup