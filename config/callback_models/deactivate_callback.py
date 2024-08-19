from aiogram.filters.callback_data import CallbackData

class Deactivate(CallbackData, prefix="dec"):
    deactivate: str