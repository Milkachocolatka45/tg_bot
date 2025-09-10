from aiogram import Router, types, F
from aiogram.filters import CommandStart,Command
from random import choice
from kbrds.reply import help_kb
from storage.data import InfoState
from aiogram.fsm.context import FSMContext
from filters.chat_types import ChatTypes

private_router = Router()
private_router.message.filter(ChatTypes(["private"]))

@private_router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer(
        "Привіт, я чудо-бот, я можу допомогти тобі зі своїми командами!",
        reply_markup=help_kb.as_markup(relaze_keyboard=True)
        )

@private_router.message(Command("help"))
async def command_help(message: types.Message):
    await message.answer("""
    /start - початок роботи
    /help - допомога
    інфо - показує інфо про тебе
    анектод - розказує анектод
    """,
        reply_markup=help_kb.as_markup(resize_keyboard=True)
        )


@private_router.message(F.text == "інфо")
async def info(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    user_id = message.from_user.id
    
    await message.answer(f"""
Твоє імʼя - {first_name}
Твоє прізвище - {last_name}
Твій username - {username}
Твій id - {user_id}
""")


@private_router.message(F.text == "анектод")
async def anektod(message: types.message):
    anekdots = [
        "Чому Python-програмісти не сваряться? Бо їм усе ясно — навіть без дужок.",
        "Як Python каже 'привіт'? — print('Hello, World!')",
        "Що скаже Python на помилку? — SyntaxError: але я тебе все одно люблю.",
        "Пайтоніст у лікаря: — У мене все відступає... — Це нормально.",
        "Python не кричить — він просто повертає None.",
        "C++: 'Я швидкий!', Java: 'Я стабільний!', Python: 'Я красивий ❤️'",
        "У Python немає скобок, бо тут усе — по-людськи.",
        "Python-програміст ніколи не самотній — у нього завжди є список.",
        "— Ти бачив той код? — Так, але він на Python. — А, тоді все гаразд.",
        "Python — єдина мова, яка змушує табуляцію бути модною."
    ]

    random_anekdots = choice(anekdots)
    await message.answer(random_anekdots)

@private_router.message(F.text == "заповни анкету")
async def fill_age(message: types.Message, state: FSMContext):
    await message.answer("Скільки тобі років?")
    await state.set_state(InfoState.age)

@private_router.message(InfoState.age)
async def fill_gener(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Ти хлопець чи дівчина?")
    await state.set_state(InfoState.gender)

@private_router.message(InfoState.gender)
async def fill_city(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await message.answer("З якого ти міста?")
    await state.set_state(InfoState.city)

@private_router.message(InfoState.city)
async def fill_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer("Введи свій номер телефону?")
    await state.set_state(InfoState.phone_number)

@private_router.message(InfoState.phone_number)
async def fill_birthday(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("Введіть дату народження")
    await state.set_state(InfoState.birthday)

@private_router.message(InfoState.birthday)
async def final(message: types.Message, state: FSMContext):
    await state.update_data(birthday=message.text)
    data = await state.get_data()
    await message.answer(f"""
Дякую за заповнення анкети!
Вік:{data["age"]}
Стать:{data["gender"]}
Місто:{data["city"]}
Номер телефону:{data["phone_number"]}
День народження:{data["birthday"]}
""")
    await state.clear()
    



