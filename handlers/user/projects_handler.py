from loader import *

projects = [
    {
        "name": "Проект №1",
        "date": "01.04.2024",
        "place": "Culture Center",
        "stud_org": "CyberHSE",
        "description": "Main Event for Dota2 HSE players",
        "tasks": "type of tasks",
        "hours": "124",
        "credits": "124/8",
    },
    {
        "name": "Проект №2",
        "date": "01.04.2024",
        "place": "Culture Center",
        "stud_org": "CyberHSE",
        "description": "Main Event for Dota2 HSE players",
        "tasks": "type of tasks",
        "hours": "124",
        "credits": "124/8",
    },
    {
        "name": "Проект №3",
        "date": "01.04.2024",
        "place": "Culture Center",
        "organization": "CyberHSE",
        "description": "Main Event for Dota2 HSE players",
        "tasks": "type of tasks",
        "hours": "124",
        "credits": "124/8",
    },
    {
        "name": "Проект №4",
        "date": "01.04.2024",
        "place": "Culture Center",
        "stud_org": "CyberHSE",
        "description": "Main Event for Dota2 HSE players",
        "tasks": "type of tasks",
        "hours": "124",
        "credits": "124/8",
    },
    {
        "name": "Проект №3",
        "date": "01.04.2024",
        "place": "Culture Center",
        "organization": "CyberHSE",
        "description": "Main Event for Dota2 HSE players",
        "tasks": "type of tasks",
        "hours": "124",
        "credits": "124/8",
    }
]

# @user_router.message(F.text == "Проекты")
# async def handle_projects(message: Message) -> None:
#     await bot.send_message(chat_id=message.chat.id,
#                            text=f'{html.italic("Ярмарка проектов")}')
    
async def get_active_events():
    try:
        # Подключение к базе данных и выборка активных событий
        database.connect()
        active_events = Event.select().where(Event.active == True)
        events_list = []
        for event in active_events:
            events_list.append(
                f"<b>{event.name}</b>\n"
                f"<i>{event.description}</i>\n"
                f"Дата начала: {event.start_date}\n"
                f"Дата окончания: {event.end_date}\n"
                f"Местоположение: {event.location}\n"
                f"Количество кредитов: {event.credits_amount}\n"
                f"Организация: {event.organization}\n"
                f"Количество часов: {event.hours_amount}\n"
                f"Формат участия: {event.part_format}\n"
            )
        database.close()
        return events_list
    except Exception as e:
        print(f"Error: {e}")
        return []

# Хендлер для команды /active_events
@user_router.message(F.text == "Проекты")
async def send_active_events(message: types.Message):
    events = await get_active_events()
    if events:
        for event in events:
            await message.answer(event, parse_mode='HTML')
    else:
        await message.answer("Нет активных событий на данный момент.")
