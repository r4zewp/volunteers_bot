from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Стейты добавления проекта
class NewProject(StatesGroup):
    name = State()
    description = State()
    start_date = State()
    end_date = State()
    location = State()
    credits_amount = State()
    organization = State()
    hours_amount = State()
    part_format = State()