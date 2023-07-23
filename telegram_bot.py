import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from chat4gpt import chatgpt
import logging
import keep_alive

load_dotenv()
bot_api = os.getenv('TELEGRAM_API')
bot = Bot(token=bot_api)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я бесплатная версия GPT 4 для телеграм. Как дела?")


@dp.message_handler()
async def handle_text(message: types.Message):
    user_message = message.text
    response = chatgpt(request=user_message)
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    keep_alive.keep_alive()
