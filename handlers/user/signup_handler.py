from loader import *

from aiogram.types import ReplyKeyboardRemove
from keyboards.edu_level_choice import edu_level_choice
from keyboards.course_number_choice import course_number_choice
from keyboards.start_markup_new import start_markup_new
from keyboards.start_markup_logged import start_markup_logged
from aiogram.types import CallbackQuery
from config.strings import *
from config.callback_models.edu_level_callback import EduLevel
from config.database import user_queries as uq
from config.cache import redis as rd

@user_router.message(Signup.phone, F.content_type.in_({'contact'}))
async def handle_phone(message: Message, state: FSMContext, conn: any):
    await state.update_data(phone=message.contact.phone_number)
    await state.update_data(username= message.from_user.username if message.from_user.username else "-")
    
    # saving user
    await bot.send_message(chat_id=message.chat.id,
                           text=f"{html.bold(html.italic('Сохраняем пользователя...'))}")
    
    data = await state.get_data()
    uid = await uq.create_user(conn, data['phone'], data['username'], message.chat.id)

    if uid:
        await state.set_state(Signup.name)
        await state.update_data(user_id=uid)
        await bot.send_message(text='Отлично, отправьте полное имя (Включая отчество, если есть)',
                           chat_id=message.chat.id,
                           reply_markup=ReplyKeyboardRemove())    
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"{html.bold(html.italic('Что-то пошло не так... пробуем снова'))}")
        await bot.send_message(chat_id=message.chat.id,
                               text=f"Отправьте телефон еще раз",
                               reply_markup=start_markup_new())

@user_router.message(Signup.name, F.content_type.in_({'text'}))
async def handle_name(message: Message, state: FSMContext):
    # мб нужно добавить проверку на ввод всякой хуйни
    await state.update_data(name=message.text)
    await state.set_state(Signup.edu_level)
    await bot.send_message(text='Теперь выбери уровень образования', 
                           chat_id=message.chat.id,
                           reply_markup=edu_level_choice())

@user_router.callback_query(Signup.edu_level, EduLevel.filter())
async def handle_edu_level(query: CallbackQuery, callback_data: EduLevel, state: FSMContext):
    await state.update_data(level=callback_data.level)
    await state.set_state(Signup.edu_course)
    await bot.send_message(chat_id=query.from_user.id,
                           text='Укажи номер курса',
                           reply_markup=course_number_choice(edu_level=callback_data.level))

@user_router.message(Signup.edu_course)
async def handle_edu_course(message: Message, state: FSMContext):
    await state.update_data(course=message.text)
    await state.set_state(Signup.edu_prog)
    await bot.send_message(chat_id=message.chat.id,
                           text="Введи название своей ОП (образовательной программы)")
    
@user_router.message(Signup.edu_prog)
async def handle_edu_prog(message: Message, conn: any, state: FSMContext):
    # saving data, finishin state
    await state.update_data(program=message.text)
    data = await state.get_data()
    await state.clear()

    await bot.send_message(chat_id=message.chat.id,
                           text=f"{html.bold(html.italic('Регистрируем...'))}")
    
    # request to save volunteer
    # vid = uq.create_volunteer(conn, data['user_id'], data)
    
    await rd.set_user_cache(telegram_id=message.chat.id)

    await bot.send_message(chat_id=message.from_user.id,
                           # работа с бдшкой, вставить пользователя 
                           text=f"{greetings_name} {html.bold('UNKNOWN')}!\n\n{greetings_action}",
                           reply_markup=start_markup_logged())



@user_router.message(Signup.phone, F.content_type.is_not({'text'}))
async def handle_name_wrong(message: Message, state: FSMContext):
    await message.reply(text="Я не понимаю такого")

