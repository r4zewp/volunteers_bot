from aiogram import types
from loader import *
from config.database import events_queries as eq
from keyboards.apply_project_markup import apply_project_markup

# Хендлер для команды /active_events
@user_router.message(F.text == "Проекты")
async def send_active_events(message: types.Message, db: any, objects: any):
   await bot.send_message(chat_id=message.from_user.id,
                          text=f'{html.italic('Загружаем список проектов...')}')
   
   events = await eq.get_active_events(objects)

   await bot.send_message(chat_id=message.from_user.id,
                          text=f'{html.bold('Активные проекты:')}')
   
   for event in events:
        event_info = f"{html.bold('Название:')} {event.name}\n" \
                    f"{html.bold('Описание:')} {event.description}\n" \
                    f"{html.bold('Дата начала:')} {event.start_date}\n" \
                    f"{html.bold('Дата окончания:')} {event.end_date}\n" \
                    f"{html.bold('Организация:')} {event.organization}" \
                    f"{html.bold('Количество часов:')} {event.hours_amount}" \
                    f"{html.bold('Количество кредитов:')} {event.credits_amount}" 
        await bot.send_message(chat_id=message.from_user.id,
                               text=event_info,
                               reply_markup=apply_project_markup(event.id))
        
      
    