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
from keyboards.start_markup_new import start_markup_new

from aiogram.types import ReplyKeyboardRemove

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
    
@user_router.message(Signup.phone, F.content_type.in_({'contact'}))
async def handle_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await state.update_data(username= message.from_user.username if message.from_user.username else "-")
    await state.set_state(Signup.name)
    await bot.send_message(text='Отлично, отправьте полное имя (Включая отчество, если есть)',
                           chat_id=message.chat.id,
                           reply_markup=ReplyKeyboardRemove())

@user_router.message(Signup.name, F.content_type.in_({'text'}))
async def handle_name(message: Message, state: FSMContext):
    # мб нужно добавить проверку на ввод всякой хуйни
    await state.update_data(name=message.text)
    data = await state.get_data()
    await message.reply('Name is ready' + data["name"])

@user_router.message(Signup.phone, F.content_type.is_not({'text'}))
async def handle_name_wrong(message: Message, state: FSMContext):
    await message.reply(text="Я не понимаю такого")

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