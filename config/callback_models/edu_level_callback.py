from aiogram.filters.callback_data import CallbackData

class EduLevel(CallbackData, prefix="lvl"):
    level: str