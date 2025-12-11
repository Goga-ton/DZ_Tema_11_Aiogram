# Этот телеграм бот сохраняет фотки, отправляет голосовые сообщения и переводит текст на английский.
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, FSInputFile
import config
from gtts import gTTS
import os
from googletrans import Translator


bot = Bot(token=config.tltok)
dp = Dispatcher()
translator = Translator()
counter=0

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer('Приветики! Я Бот! Хочешь узнать что могу спроси меня командой "/help" ')

@dp.message(Command('help'))
async def help(message:Message):
    await message.answer('1. Если ты пришлешь мне фотки тоя их сохраню для потомков '
                         '\n2) Если напишешь текст через команду "/voice" я пришлю еего тебе в сообщении" '
                         '\n3) Если просто напишешь мне, то я тебе переведу все написанное тобой на английский')

class RecordVoice(StatesGroup):
    waiting_voice = State()

@dp.message(Command('voice'))
async def voice(message:Message, state: FSMContext):
    await message.answer("Введите текст для формирования сообщения:")
    await state.set_state(RecordVoice.waiting_voice)

@dp.message(RecordVoice.waiting_voice)
async def rec_voice(message:Message, state: FSMContext):
    tts = gTTS(text=message.text, lang='ru') #text=message.text.strip() - strip убирает пробелы в начале и конце строки
    tts.save('voiceover.ogg')
    await message.answer_voice(FSInputFile('voiceover.ogg'))
    os.remove('voiceover.ogg')
    await state.clear()

@dp.message(F.photo)
async def photo(message: Message):
    global counter
    counter += 1
    filename = f"img/Фото-{counter}.jpg"
    await bot.download(message.photo[-1], destination=filename)
    await message.answer(f"Твоя фотка сохранено для потомков, ее название: 'Фото-{counter}.jpg'")


@dp.message(F.text) # эхо бот, отвечает тем что ты ему написал
async def eho(message: Message):
    # Переводим на английский
    result = await translator.translate(message.text, dest="en")
    await message.answer(result.text)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
