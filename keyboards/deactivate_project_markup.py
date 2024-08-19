from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import *
from config.callback_models.deactivate_callback import Deactivate

def deactivate_project_markup(*, project_id: int) -> InlineKeyboardMarkup:
    deact = InlineKeyboardButton(text='📝 Деактивировать проект', callback_data=Deactivate(deactivate=f'deactivate_{project_id}').pack())
    
    markup = InlineKeyboardMarkup(inline_keyboard=[[deact]])

    return markup
