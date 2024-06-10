from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import *
from config.callback_models.decide_callback import Decide

def decide_on_request_markup(user_id, project_id) -> InlineKeyboardMarkup:
    approve = InlineKeyboardButton(text="Разрешить", callback_data=Decide(decision=f"approve_{user_id}_{project_id}").pack())
    decline = InlineKeyboardButton(text="Отклонить", callback_data=Decide(decision=f"decline_{user_id}_{project_id}").pack())

    markup = InlineKeyboardMarkup(inline_keyboard=[[approve, decline]])

    return markup