import asyncio
from random import randint

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import config
import random

bot = Bot(token=config.tltok)
dp = Dispatcher()

@dp.message(Command('photo'))
async def photo(message:Message):
    list1 = ['https://cs8.pikabu.ru/post_img/2016/09/28/7/og_og_147506151225418488.jpg',
            'https://wallpapers.com/images/hd/kitten-pictures-uia1gi79yw5himz4.jpg',
            'https://i.pinimg.com/474x/e2/17/b7/e217b73583daf729b12010f7e475acfa.jpg']
    rdfoto = random.choice(list1)
    await message.answer_photo(photo=rdfoto, caption='"Это подпись фотки"')

@dp.message(F.photo)
async def answ_foto(message:Message):
    list = ['ОГО крутая ФОТКА', 'Фотка клас', 'Фотка БЭ']
    answ_foto = random.choice(list)
    await message.answer(answ_foto)

@dp.message(F.text == "Что такое ИИ")
async def aitext(message:Message):
    await message.answer('Искусственный интеллект (ИИ, искусственный разум, AI) '
                         '— термин, который означает разработку компьютерных систем, '
                         'способных выполнять задачи, свойственные человеческому интеллекту. '
                         'Это включает анализ данных, распознавание образов, обработку текстов и запросов, '
                         'сформулированных естественным языком, обучение на потоках данных и принятие решений.')

@dp.message(Command('help'))
async def help(message:Message):
    await message.answer('Это очень КРУТОЙ помощник на Ваши запросы')

@dp.message(CommandStart)
async def start(message:Message):
    await message.answer('Приветики! Я Бот!')




async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


