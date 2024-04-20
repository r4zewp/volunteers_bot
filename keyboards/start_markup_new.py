from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_markup_new():
    share_phone = KeyboardButton(text='Поделиться номером телефона', request_contact=True)
    return ReplyKeyboardMarkup(keyboard=[[share_phone]], resize_keyboard=True)
