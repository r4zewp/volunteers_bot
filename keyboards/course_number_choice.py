from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def course_number_choice(edu_level):

    first = KeyboardButton(text="1")
    second = KeyboardButton(text="2")
    third = KeyboardButton(text="3")
    fourth = KeyboardButton(text="4")

    if edu_level == "masters":
        markup = ReplyKeyboardMarkup(keyboard=[[first, second]], resize_keyboard=True)
    else:
        markup = ReplyKeyboardMarkup(keyboard=[[first, second], [third, fourth]], resize_keyboard=True)

    return markup