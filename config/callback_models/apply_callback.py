from aiogram.filters.callback_data import CallbackData

class Apply(CallbackData, prefix="my"):
    apply: str