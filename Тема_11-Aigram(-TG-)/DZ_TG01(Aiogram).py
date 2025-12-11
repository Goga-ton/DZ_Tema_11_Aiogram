# Этот телеграм бот отвечает на команды и парсит погоду для города по команде city. команды с которыми он работает смотри в коде.
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

@dp.message(Command('photo'))
async def photo(message:Message):
    list1 = ['https://cs8.pikabu.ru/post_img/2016/09/28/7/og_og_147506151225418488.jpg',
            'https://wallpapers.com/images/hd/kitten-pictures-uia1gi79yw5himz4.jpg',
            'https://i.pinimg.com/474x/e2/17/b7/e217b73583daf729b12010f7e475acfa.jpg']
    rdfoto = random.choice(list1)
    await message.answer_photo(photo=rdfoto, caption='"Это фотка подобранная ИИ под твое настроение"')

@dp.message(F.photo)
async def answ_foto(message:Message):
    list = ['ОГО крутая ФОТКА', 'Фотка клас', 'Фотка БЭ']
    answ_foto = random.choice(list)
    await message.answer(answ_foto)

# @dp.message(F.text == "Что такое ИИ")
# async def aitext(message:Message):
#     await message.answer('Искусственный интеллект (ИИ, искусственный разум, AI) '
#                          '— термин, который означает разработку компьютерных систем, '
#                          'способных выполнять задачи, свойственные человеческому интеллекту. '
#                          'Это включает анализ данных, распознавание образов, обработку текстов и запросов, '
#                          'сформулированных естественным языком, обучение на потоках данных и принятие решений.')

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer('Приветики! Я Бот!')

@dp.message(Command('help'))
async def help(message:Message):
    await message.answer('В Данном Telegram боте ты сможешь: \n1) Получить оценку фотографии загрузив ее; \n2) Узнать погоду в городе введя его название;'
                         '\n3) Получить класную фотку соответсвующею твоему настроению.')

class WeatherStates(StatesGroup):
    waiting_city = State()


@dp.message(Command("city"))
async def city_command(message:Message, state: FSMContext):
    await message.answer("Введите название города:")
    await state.set_state(WeatherStates.waiting_city)


@dp.message(WeatherStates.waiting_city)
async def get_city_weather(message:Message, state: FSMContext):
    city = message.text.strip()

    ap_key = config.api_key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={ap_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            await message.answer(
                f"🌤️ Погода в {data['name']}:\n"
                f"Температура: {data['main']['temp']}°C\n"
                f"Ощущается как: {data['main']['feels_like']}°C\n"
                f"Описание: {data['weather'][0]['description']}\n"
                f"Влажность: {data['main']['humidity']}%"
            )
        else:
            await message.answer("❌ Город не найден")

    except:
        await message.answer("❌ Ошибка получения данных")

    await state.clear()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
