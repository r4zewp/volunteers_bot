from loader import *

# database
from config.database import user_queries as uq
from config.cache.redis import get_redis

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

@user_router.message(CommandStart())
async def command_start_handler(message: Message, conn: any) -> None:
    # Должна быть проверка на существование пользователя
    # в базе данных
    #
    # Пока допускаем, что пользователь уже существует
    # # Далее должна идти проверка на пользователя -> дальше понять, как
    # # мб сторить глобально тип пользователя, чтобы постоянно не обращаться к БД
    
    # try:   
        redis = await get_redis()
        cached_user = await redis.get(f"user_id:{message.chat.id}")
        
        if cached_user:
            decoded = cached_user.decode('utf-8')
            await bot.send_message(chat_id=message.chat.id,
                                   text=decoded)
        else:
            user = await uq.get_user(conn, message.chat.id)
            if user:
                await redis.setex("user_id", 9999, message.chat.id)
                await bot.send_message(chat_id=message.from_user.id, 
                                text=greetings,
                                reply_markup=start_markup_logged())
            else:
                await bot.send_message(chat_id=message.from_user.id, text="NOT EXIST")

    # except Exception:
    #     print('exception')

@user_router.message()
async def handle_unknown(message: Message) -> None:
    await bot.send_message(chat_id=message.chat.id,
                           text=unknown)

async def main(): 
    dp = Dispatcher()

    dp.include_router(user_router)

    pool = await database.create_pool()
    user_router.message.middleware(middleware.DbMiddleware(pool))
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())