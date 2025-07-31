from aiogram import Router, types, F
from aiogram.filters import CommandStart,Command
from random import choice
from kbrds.reply import help_kb

private_router = Router()

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
    анектод - розказує анектод""")

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