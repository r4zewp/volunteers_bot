from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Стейты регистрации нового студента
class Signup(StatesGroup):
    name = State()
    edu_prog = State()
    phone = State()