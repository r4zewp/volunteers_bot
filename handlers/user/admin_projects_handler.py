from aiogram import types
from loader import *
from config.database import events_queries as eq
from config.database import volunteer_queries as vq
from keyboards.deactivate_project_markup import deactivate_project_markup
from config.callback_models.deactivate_callback import Deactivate

@user_router.message(F.text == "Все проекты")
async def send_active_events(message: Message, db: any, objects: any):
   await bot.send_message(chat_id=message.from_user.id,
                          text=f'{html.italic("Загружаем список проектов...")}')
   
   events = await eq.get_active_events(objects)
   await bot.send_message(chat_id=message.from_user.id,
                          text=f'{html.bold("Активные проекты:")}')
   
   for event in events:
        event_info = f"{html.bold('Название:')} {event.name}\n" \
                    f"{html.bold('Описание:')} {event.description}\n" \
                    f"{html.bold('Дата начала:')} {event.start_date}\n" \
                    f"{html.bold('Дата окончания:')} {event.end_date}\n" \
                    f"{html.bold('Организация:')} {event.organization}\n" \
                    f"{html.bold('Количество часов:')} {event.hours_amount}\n" \
                    f"{html.bold('Количество кредитов:')} {event.credits_amount}\n" 
        await bot.send_message(chat_id=message.from_user.id,
                               text=event_info,
                               reply_markup=deactivate_project_markup(project_id=event.e_id))
        
@user_router.message(F.text == "Все волонтеры")
async def send_active_events(message: Message, db: any, objects: any):
   await bot.send_message(chat_id=message.from_user.id,
                          text=f'{html.italic("Загружаем список волонтеров...")}')
   
   volunteers = await vq.get_all_volunteers(objects)
   await bot.send_message(chat_id=message.from_user.id,
                          text=f'{html.bold("Волонтеры:")}')
   
   for voln in volunteers:
        vif = f"{html.bold('Имя:')} {voln.name} {voln.surname}\n" \
                    f"{html.bold('Уровень образования:')} {voln.education_type}\n" \
                    f"{html.bold('Программа обучения:')} {voln.education_program}\n" \
                    f"{html.bold('Номер курса:')} {voln.course_number}\n" 
        await bot.send_message(chat_id=message.from_user.id,
                               text=vif)