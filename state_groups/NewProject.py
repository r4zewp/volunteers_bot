from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Стейты добавления проекта
class NewProject(StatesGroup):
    name = State()
    credits_total = State()