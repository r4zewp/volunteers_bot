from aiogram import types
from loader import *
    

# Хендлер для команды /active_events
@user_router.message(F.text == "Проекты")
async def send_active_events(message: types.Message):
    events = []
    #
    if events:
        for event in events:
            await message.answer(event, parse_mode='HTML')
    else:
        await message.answer("Нет активных событий на данный момент.")
