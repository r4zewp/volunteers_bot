from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import *
from config.callback_models.apply_callback import Apply

def apply_project_markup(*, project_id: int) -> InlineKeyboardMarkup:
    apply = InlineKeyboardButton(text='📝 Подать заявку', callback_data=Apply(apply=f'apply_project_{project_id}').pack())
    
    markup = InlineKeyboardMarkup(inline_keyboard=[[apply]])

    return markup
