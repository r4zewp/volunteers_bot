from loader import *

@dp.message(F.text == "Табель")
async def handle_projects(message: Message) -> None:
    await bot.send_message(chat_id=message.chat.id,
                           text='GRADES')