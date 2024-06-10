from aiogram.filters.callback_data import CallbackData

class Decide(CallbackData, prefix="dec"):
    decision: str