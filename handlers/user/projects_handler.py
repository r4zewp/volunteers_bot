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

@user_router.message(F.text == "Проекты")
async def handle_projects(message: Message) -> None:
    await bot.send_message(chat_id=message.chat.id,
                           text=f'{html.italic("Ярмарка проектов")}')