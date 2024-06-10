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

@user_router.message(NewProject.name, F.content_type.in_({'text'}))
async def handle_name(message: Message, state: FSMContext, db: any, objects: any):
    await state.update_data(name=message.text)
    await state.set_state(NewProject.description)
    await bot.send_message(text='Введите подробное описание проекта',
                           chat_id=message.chat.id)