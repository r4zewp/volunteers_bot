from loader import *

@dp.message(F.text == "Профиль")
async def handle_profile(message: Message) -> None:
    await bot.send_message(chat_id=message.chat.id, 
                           text='Profile')