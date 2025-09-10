from aiogram import Bot, Dispatcher, types
import asyncio
from handlers.private_handlers import private_router
from handlers.group_handlers import group_router

TOKEN = "8346367890:AAEcbSkkUsNnBcqX73ZbYWw3lywQuR4OlTs"

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(private_router)
dp.include_router(group_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    print("Bot is running...")


asyncio.run(main())