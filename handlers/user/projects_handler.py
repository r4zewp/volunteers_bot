from aiogram import types
from loader import *
from config.database import events_queries as eq

from config.callback_models.apply_callback import Apply
from config.callback_models.decide_callback import Decide
from aiogram.types import CallbackQuery

from keyboards.apply_project_markup import apply_project_markup
from keyboards.decide_on_request_markup import decide_on_request_markup

# Хендлер для команды /active_events
@user_router.message(F.text == "Проекты")
async def send_active_events(message: types.Message, db: any, objects: any):
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
                               reply_markup=apply_project_markup(project_id=event.e_id))

@user_router.callback_query(Apply.filter())
async def handle_apply(message: Message, callback_data: Apply):

    #await bot.send_message('Ваша заявка была успешно отправлена. Ожидайте ответа!')

    await bot.send_message(chat_id=message.from_user.id,
                           text=f'{html.italic("Обрабатываем вашу заявку...")}')
    
    project_id = callback_data.apply.split("_")[2]

    await bot.send_message(chat_id=-1002165509651, 
                           text=f'Поступила заявка от {message.from_user.username} '\
                            f'на проект {project_id}.\n\nПримите ' \
                            f'по ней решение кнопкой снизу',
                            reply_markup=decide_on_request_markup(message.from_user.id, 
                                                                  project_id))
    
    await bot.send_message(chat_id=message.from_user.id,
                           text="Ваша заявка была успешно отправлена. \n\nОжидайте ответа!")

@user_router.callback_query(Decide.filter())
async def handle_decision(message: Message, callback_data: Decide):
    decision_data = callback_data.decision
    await bot.send_message(chat_id=-1002165509651,
                            text=decision_data)
        
      
    