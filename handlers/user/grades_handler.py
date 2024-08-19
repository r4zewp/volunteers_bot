from loader import *

@user_router.message(F.text == "Табель")
async def handle_projects(message: Message) -> None:
    await bot.send_message(chat_id=message.chat.id,
                           text=f'{html.bold("Мои проекты")}\n\n'\
                           f'{html.bold("Проект 1")}\n' \
                           'Зачтенные часы: 8ч\nКредиты: 1'
                           )
    
#     # handling unknown messages
# @user_router.message()
# async def handle_unknown(message: Message) -> None:
#     await bot.send_message(chat_id=message.chat.id,
#                            text=unknown)