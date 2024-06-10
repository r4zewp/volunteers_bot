from loader import *
from keyboards.profile import create_profile_kb
from config.database import volunteer_queries as vq
from config.database import user_queries as uq

@user_router.message(F.text == "Профиль")
async def handle_profile(message: Message, db: any, objects: any) -> None:
    
    # заменить запросом к бд
    user = await uq.get_user_by_id(message.from_user.id, objects=objects)
    volunteer = await vq.get_volunteer_by_user_id(user.id, objects)

    await bot.send_message(chat_id=message.chat.id, 
                           text=create_profile(volunteer.name,
                                               volunteer.surname,
                                               volunteer.middlename,
                                               volunteer.education_program,
                                               "Бакалавриат" if volunteer.education_type == "bachelor" else "Магистратура",
                                               volunteer.course_number),
                            reply_markup=create_profile_kb())
                                               