from aiogram.fsm.state import StatesGroup, State

class InfoState(StatesGroup):
    age = State()
    gender = State()
    city = State()
    phone_number = State()
    birthday = State()
