import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from handlers import handle_post

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("post"))
async def handle_post_command(message: types.Message):
    await handle_post(message)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
