from loader import *

# handlers
## user
from handlers.user import profile_handler
from handlers.user import grades_handler
from handlers.user import projects_handler

## admin

## manager

# keyboards
from keyboards.start_markup_logged import start_markup_logged

# config
from config.strings import *



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # Должна быть проверка на существование пользователя
    # в базе данных
    #
    # Пока допускаем, что пользователь уже существует
    # # Далее должна идти проверка на пользователя -> дальше понять, как
    # # мб сторить глобально тип пользователя, чтобы постоянно не обращаться к БД
    await bot.send_message(chat_id=message.from_user.id, 
                           text=greetings,
                           reply_markup=start_markup_logged())

@dp.message()
async def handle_unknown(message: Message) -> None:
    await bot.send_message(chat_id=message.chat.id,
                           text=unknown)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())