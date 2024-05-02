from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.callback_models.edu_level_callback import EduLevel

def edu_level_choice():

    bachelor = InlineKeyboardButton(text="Бакалавриат", callback_data=EduLevel(level="bachelor").pack())
    masters = InlineKeyboardButton(text="Магистратура", callback_data=EduLevel(level="masters").pack())

    markup = InlineKeyboardMarkup(inline_keyboard=[[bachelor, masters]])

    return markup