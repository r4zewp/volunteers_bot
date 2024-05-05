from loader import *
from keyboards.profile import create_profile_kb

profile_mock = {
    "name": "Tigran",
    "surname": "Arustamov",
    "middlename": "-",
    "course_number": "1",
    "program": "Бизнес-информатика",
    "level": "Бакалавриат"
}


@user_router.message(F.text == "Профиль")
async def handle_profile(message: Message) -> None:
    
    # заменить запросом к бд
    profile = profile_mock    

    await bot.send_message(chat_id=message.chat.id, 
                           text=create_profile(profile['name'],
                                               profile['surname'],
                                               profile['middlename'],
                                               profile['program'],
                                               profile['level'],
                                               profile['course_number'],),
                            reply_markup=create_profile_kb())
                                               