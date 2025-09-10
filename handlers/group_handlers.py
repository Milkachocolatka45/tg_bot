from aiogram import Router, F, types
from filters.chat_types import ChatTypes

group_router = Router()
group_router.message.filter(ChatTypes(["group", "supergroup"]))

warned_users = {}

restricted_words = {"козел", "дебіл", "олень"}

@group_router.message()
async def ban_detector(message: types.Message):
    if restricted_words.intersection(message.text.lower().split(" ")):
        warn_user_id = message.from_user.id
        if warn_user_id in warned_users:
            warned_users[warn_user_id] = warned_users[warn_user_id] + 1
        else:
            warned_users[warn_user_id] = 1
        print(warned_users)
        await message.answer(f"{message.from_user.first_name} {message.from_user.last_name} будьте ввічливі! Це Ваше {warned_users[warn_user_id]} попередження!")
        await message.delete()
