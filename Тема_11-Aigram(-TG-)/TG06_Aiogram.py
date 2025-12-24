#Бот будет регистрировать тебя и смотреть курс валют через API + советы по экономии + будем вести расходы по трем категориям
import asyncio

import requests
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import config
import TG06_keyboards as kb
import random
from gtts import gTTS
import sqlite3

bot = Bot(token=config.tltok)
dp = Dispatcher()
conn = sqlite3.connect('user_bd.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    name TEXT,
    category1 TEXT,
    category2 TEXT,
    category3 TEXT,
    expenses1 REAL,
    expenses2 REAL,
    expenses3 REAL
    )
''')
conn.commit()

class FinancesForm(StatesGroup):
    category1 = State()
    category2 = State()
    category3 = State()
    expenses1 = State()
    expenses2 = State()
    expenses3 = State()

@dp.message (CommandStart())
async def send_start(message: Message):
    await message.answer('Привет! Я Ваш личный финансовый помошник. Выберете один пункт меню.', reply_markup=kb.keyboard)

@dp.message (F.text == 'Регистрация в TGBot')
async def registration(message: Message):
    telega_id = message.from_user.id
    name = message.from_user.full_name
    cursor.execute('''SELECT * FROM users WHERE telegram_id = ?''', (telega_id,))
    user = cursor.fetchone() # берет первый вариант
    if user:
        await message.answer('Вы уже зарегестрированы')
    else:
        cursor.execute('''INSERT INTO users (telegram_id, name) VALUES (?, ?)''', (telega_id, name))
        conn.commit()
        await message.answer('Вы успешно зарегестрированы')

@dp.message (F.text == 'Курс валют')
async def but_kyrs_val(message: Message):
    url = f'https://v6.exchangerate-api.com/v6/{config.exch_apikey}/latest/USD'
    try:
        response = requests.get(url)
        valuta = response.json()
        if response.status_code != 200:
            await message.answer('Не удалось получить котировку!')
            return
        usd_to_rub = valuta['conversion_rates']['RUB'] # Путь в API сперва название справочника, потом ключ
        usd_to_eur = valuta['conversion_rates']['EUR']
        eur_to_rub = usd_to_rub * usd_to_eur

        await message.answer(f'RUB - {usd_to_rub:.2f} RUB\n'
                             f'RUB - {eur_to_rub:.2f} RUB\n')
    except:
        await message.answer('Произошла ошибка')

@dp.message(F.text == 'Советы начинающим инвесторам')
async def but_tips(message: Message):
    tips = [
        "Совет 1: Ведите бюджет и следите за своими расходами.",
        "Совет 2: Откладывайте часть доходов на сбережения.",
        "Совет 3: Покупайте товары по скидкам и распродажам."
    ]
    tip = random.choice(tips)
    await message.answer(tip)

@dp.message(F.text == 'Расходы')
async def but_fin_c1(message: Message, state:FSMContext):
    await state.set_state(FinancesForm.category1)
    await message.reply('Введите первую категорию расходов')

@dp.message(FinancesForm.category1)
async def but_fin_e1(message: Message, state:FSMContext):
    await state.update_data(category1 = message.text)
    await state.set_state(FinancesForm.expenses1)
    await message.reply('Введите расходы для категории №1')

@dp.message(FinancesForm.expenses1)
async def but_fin_c2(message: Message, state:FSMContext):
    await state.update_data(expenses1 = float(message.text))
    await state.set_state(FinancesForm.category2)
    await message.reply('Введите вторую категорию расходов')

@dp.message(FinancesForm.category2)
async def but_fin_e2(message: Message, state:FSMContext):
    await state.update_data(category2 = message.text)
    await state.set_state(FinancesForm.expenses2)
    await message.reply('Введите расходы для категории №2')

@dp.message(FinancesForm.expenses2)
async def but_fin_c3(message: Message, state:FSMContext):
    await state.update_data(expenses2 = float(message.text))
    await state.set_state(FinancesForm.category3)
    await message.reply('Введите третью категорию расходов')

@dp.message(FinancesForm.category3)
async def but_fin_e3(message: Message, state:FSMContext):
    await state.update_data(category3 = message.text)
    await state.set_state(FinancesForm.expenses3)
    await message.reply('Введите расходы для категории №3')

@dp.message(FinancesForm.expenses3)
async def finances(message: Message, state:FSMContext):
    data = await state.get_data()
    telegram_id = message.from_user.id
    cursor.execute('''
    UPDATE users SET category1 = ?, expenses1 = ?, category2 = ?, expenses2 = ?, category3 = ?, expenses3 = ? WHERE telegram_id = ?''',
                   (data['category1'], data['expenses1'], data['category2'], data['expenses2'], data['category3'], float(message.text), telegram_id))
    conn.commit()
    await state.clear()

    await message.answer('Категории и расходы сохранены')


async def main():
    await dp.start_polling(bot) #Ваш бот использует polling — программа сама "стучится" к Telegram и распределяет сообщения по хендлерам по фильтрам.

if __name__ == '__main__':
    asyncio.run(main())


