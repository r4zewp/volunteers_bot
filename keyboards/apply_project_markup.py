from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import *

def apply_project_markup(*, project_id: int) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text='📝 Откликнуться', callback_data=f'apply_project_{project_id}'))
    return markup
