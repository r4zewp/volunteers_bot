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
from config.database import volunteer_queries as vq
from config.cache import redis as rd
from state_groups.NewProject import NewProject
from config.database.events_queries import *

@user_router.message(F.text == "Создать проект")
async def create_project(message: Message, objects: any):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Введите название проекта')

@user_router.message(NewProject.name, F.content_type.in_({'text'}))
async def handle_name(message: Message, state: FSMContext, db: any, objects: any):
    await state.update_data(name=message.text)
    await state.set_state(NewProject.description)
    await bot.send_message(text='Введите подробное описание проекта',
                           chat_id=message.chat.id,)

@user_router.message(NewProject.description, F.content_type.in_({'text'}))
async def handle_description(message: Message, state: FSMContext, db: any, objects: any):
    await state.update_data(description=message.text)
    await state.set_state(NewProject.start_date)
    await bot.send_message(text='Выберите дату старта проекта',
                           chat_id=message.chat.id,)

@user_router.message(NewProject.start_date, F.content_type.in_({'text'}))
async def handle_sdate(message: Message, state: FSMContext, db: any, objects: any):
    await state.update_data(start_date=message.text)
    await state.set_state(NewProject.end_date)
    await bot.send_message(text='Выберите дату окончания проекта',
                           chat_id=message.chat.id,)
    
@user_router.message(NewProject.end_date, F.content_type.in_({'text'}))
async def handle_edate(message: Message, state: FSMContext, db: any, objects: any):
    await state.update_data(end_date=message.text)
    await state.set_state(NewProject.location)
    await bot.send_message(text='Укажите место проведения проекта',
                           chat_id=message.chat.id,)
    
@user_router.message(NewProject.location, F.content_type.in_({'text'}))
async def handle_loc(message: Message, state: FSMContext, db: any, objects: any):
    await state.update_data(location=message.text)
    await state.set_state(NewProject.credits_amount)
    await bot.send_message(text='Укажите количество кредитов за проект',
                           chat_id=message.chat.id,)
   

@user_router.message(NewProject.credits_amount, F.content_type.in_({'text'}))
async def handle_cred_amount(message: Message, state: FSMContext, db: any, objects: any):
    await state.update_data(credits_amount=message.text)
    await state.set_state(NewProject.organization)
    await bot.send_message(text='Укажите наименование организации',
                           chat_id=message.chat.id,)
    
@user_router.message(NewProject.organization, F.content_type.in_({'text'}))
async def handle_org(message: Message, state: FSMContext, db: any, objects: any):
    await state.update_data(organization=message.text)
    await state.set_state(NewProject.hours_amount)
    await bot.send_message(text='Укажите требуемое коллиство часов на проекте',
                           chat_id=message.chat.id,)
    
@user_router.message(NewProject.hours_amount, F.content_type.in_({'text'}))
async def handle_hours_amount(message: Message, state: FSMContext, db: any, objects: any):
    await state.update_data(hours_amount=message.text)
    await state.set_state(NewProject.part_format)
    await bot.send_message(text='Укажите формат участия',
                           chat_id=message.chat.id,)
    
@user_router.message(NewProject.part_format, F.content_type.in_({'text'}))
async def handle_part_format(message: Message, state: FSMContext, db: any, objects: any):
    await state.update_data(part_format=message.text)
    await state.set_state(NewProject.start_date)
    
    data = await state.get_data()

    await bot.send_message(text='Проект успешно создан!',
                           chat_id=message.chat.id,)
    
    create_event(data)
    