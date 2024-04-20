from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Стейты регистрации нового студента
class Signup(StatesGroup):
    phone = State() # Номер телефона + юзернейм
    name = State() # Полное имя
    edu_level = State() # Образовательный уровень
    edu_prog = State() # Образовательная программа
    edu_course = State() # Курс
    