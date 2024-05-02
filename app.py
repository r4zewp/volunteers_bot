from loader import *

# database
from config.database import user_queries as uq
from config.cache.redis import get_redis

# handlers
## user
from handlers.user import profile_handler
from handlers.user import grades_handler
from handlers.user import projects_handler
from handlers.user import signup_handler

## admin

## manager

# keyboards
from keyboards.start_markup_logged import start_markup_logged
from keyboards.start_markup_new import start_markup_new


# config
from config.strings import *

@user_router.message(CommandStart())
async def command_start_handler(message: Message, conn: any, state: FSMContext) -> None:
    
    try:  
        # формируем ключ пользователя для редиса
        user_key = "user_id_" + str(message.chat.id)

        # инициируем редис, ищем по ключу пользователя
        # если есть, декодим в utf-8 и делаем дела дальшe
        redis = await get_redis()
        cached_user = await redis.get(user_key)

        if cached_user:
            decoded = cached_user.decode('utf-8')
            await bot.send_message(chat_id=message.chat.id,
                                   text=decoded)
            await redis.close()

        # если нет, то смотрим, есть ли такой юзер в бд
        # если есть, закидываем в кэш и делаем дела дальше
        else:
            user = await uq.get_user(conn, message.chat.id)
            if user:
                await redis.setex(user_key, 9999, message.chat.id)
                await bot.send_message(chat_id=message.from_user.id, 
                                text=f"{greetings_name} {html.bold(user['user']['username'])}!\n\n{greetings_action}",
                                reply_markup=start_markup_logged())
                await redis.close()
                
        # # если нет, то отправляем по процессу регистрации
            else:
                await state.set_state(Signup.phone)
                await bot.send_message(chat_id=message.from_user.id, 
                                       text=greetings_new,
                                       reply_markup=start_markup_new())

    except Exception as e:
        print(e)
    
# handling unknown messages

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