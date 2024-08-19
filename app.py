from loader import *

# database
from config.database import user_queries as uq
from config.database import events_queries as eq
from config.database import volunteer_queries as vq
from config.cache.redis import get_redis
from config.models.User import User
from config.models.Volunteer import Volunteer
from config.models.Event import Event
from config.models.Volunteer_X_Event import Volunteer_X_Event

from keyboards.deactivate_project_markup import deactivate_project_markup
from config.callback_models.deactivate_callback import Deactivate

# handlers
## user
from handlers.user import profile_handler
from handlers.user import grades_handler
from handlers.user import projects_handler
from handlers.user import signup_handler
from handlers.user import admin_projects_handler
from handlers.admin import create_project_handler

## admin

## manager

# keyboards
from keyboards.start_markup_logged import start_markup_logged
from keyboards.start_markup_new import start_markup_new
from keyboards.create_admin_menu import create_admin_kb

# config
from config.strings import *
from config.database.database import create_pool

@user_router.message(Command('admin'))
async def handle_command(message: Message, db: any, objects: any):
    user = await uq.get_user_by_id(message.from_user.id,
                            objects=objects)
    if user.is_admin:
        await bot.send_message(chat_id=message.from_user.id, 
                               text='Меню управления',
                               reply_markup=create_admin_kb())
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text='У вас нет доступа к этой команде')

@user_router.message(CommandStart())
async def command_start_handler(message: Message, db: any, objects: any, state: FSMContext) -> None:
    
    try:  
        # формируем ключ пользователя для редиса
        user_key = "user_id_" + str(message.chat.id)

        # инициируем редис, ищем по ключу пользователя
        # если есть, декодим в utf-8 и делаем дела дальшe
        redis = await get_redis()
        cached_user = await redis.get(user_key)

        if cached_user:
            user = await uq.get_user_by_id(message.chat.id, objects=objects)
            
            if user:
                
                volunteer = await vq.get_volunteer_by_user_id(user.id, objects=objects)
                
                if volunteer:
                    await bot.send_message(chat_id=message.from_user.id, 
                                    text=f"{greetings_name} {html.bold(volunteer.name)}!\n\n{greetings_action}",
                                    reply_markup=start_markup_logged())
                else:
                    await state.set_state(Signup.phone)
                    await bot.send_message(chat_id=message.from_user.id, 
                                       text=greetings_new,
                                       reply_markup=start_markup_new())
            else:
                await state.set_state(Signup.phone)
                await bot.send_message(chat_id=message.from_user.id, 
                                       text=greetings_new,
                                       reply_markup=start_markup_new())
            
            await redis.close()

        # если нет, то смотрим, есть ли такой юзер в бд
        # если есть, закидываем в кэш и делаем дела дальше
        else:
            user = await uq.get_user_by_id(message.chat.id, objects=objects)
            if user:

                volunteer = await vq.get_volunteer_by_user_id(user.id, objects)

                if volunteer:
                    await redis.setex(user_key, 9999, message.chat.id)
                    await bot.send_message(chat_id=message.from_user.id, 
                                    text=f"{greetings_name} {html.bold(volunteer.name)}!\n\n{greetings_action}",
                                    reply_markup=start_markup_logged())
                    
                else:
                    await state.set_state(Signup.phone)
                    await bot.send_message(chat_id=message.from_user.id, 
                                       text=greetings_new,
                                       reply_markup=start_markup_new())
                
                
        # # если нет, то отправляем по процессу регистрации
            else:
                await state.set_state(Signup.phone)
                await bot.send_message(chat_id=message.from_user.id, 
                                       text=greetings_new,
                                       reply_markup=start_markup_new())

    except Exception as e:
        print(e)


@user_router.callback_query(Deactivate.filter())
async def deactivate_project(message: Message, callback_data: Deactivate, objects: any):
    project_id = callback_data.deactivate.split("_")[1]
    



async def main(): 
    dp = Dispatcher()
    dp.include_router(user_router)
    db, objects = await create_pool()

    with db:
        db.create_tables([User, Volunteer, Event, Volunteer_X_Event])

    user_router.message.middleware(middleware.DbMiddleware(db=db, objects=objects))
    user_router.callback_query.middleware(middleware.DbMiddleware(db=db, objects=objects))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, 
                        stream=sys.stdout,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',)
    asyncio.run(main())