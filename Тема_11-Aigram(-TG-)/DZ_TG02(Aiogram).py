# Этот телеграм бот сохраняет фотки, отправляет голосовые сообщения и переводит текст на английский.
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
import config
import random
import requests



bot = Bot(token=config.tltok)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer('Приветики! Я Бот!')

@dp.message(Command('help'))
async def help(message:Message):
    await message.answer('В Данном Telegram боте ты сможешь: \n1) Получить оценку фотографии загрузив ее; \n2) Узнать погоду в городе введя его название;'
                         '\n3) Получить класную фотку соответсвующею твоему настроению.')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
