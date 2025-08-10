from aiogram import Bot, Dispatcher, types
import asyncio
from handlers.handlers import private_router

TOKEN = "8346367890:AAEcbSkkUsNnBcqX73ZbYWw3lywQuR4OlTs"

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(private_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    print("Bot is running...")


asyncio.run(main())