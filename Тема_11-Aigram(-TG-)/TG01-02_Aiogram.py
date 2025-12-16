import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import config
import TG04_keyboards as kb
import random
from gtts import gTTS
import os


bot = Bot(token=config.tltok)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(f'Приветики, {message.from_user.full_name}', reply_markup=await kb.list_kb()) #указывает имя пользователя (reply_markup=kb.keyb - добавляет кнопки)

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Это очень КРУТОЙ помощник на Ваши запросы', reply_markup=kb.keyb) # или можно "reply_markup=kb.keyb_inl"

@dp.message(Command('city'))
async def city(message: Message):
    await message.answer('Это меню по предоставлению Инвайтных битонов!! :)', reply_markup=kb.keyb_inl) # или можно "reply_markup=kb.keyb_inl"

@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
    await callback.answer('Новости подгружаются', show_alert=True) # уведомление о происходящем действии, если убрать "show_alert=True" то будет просто всплывающая надпись, а так окно с кнопочкой
    await callback.message.answer('Вот свежие новости')

@dp.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Каталог обновляется') # уведомление о происходящем действии, всплывающая надпись.
    await callback.message.edit_text('Вот актуальные данные о каталоге', reply_markup=await kb.list_kb_inv())

@dp.message(F.text == 'Test-1')
async def test(message: Message):
    await message.answer('Обработка нажатия на КНОПКУ')


@dp.message(Command('photo', prefix="-"))
async def photo(message:Message):
    list1 = ['https://cs8.pikabu.ru/post_img/2016/09/28/7/og_og_147506151225418488.jpg',
            'https://wallpapers.com/images/hd/kitten-pictures-uia1gi79yw5himz4.jpg',
            'https://i.pinimg.com/474x/e2/17/b7/e217b73583daf729b12010f7e475acfa.jpg']
    rdfoto = random.choice(list1)
    await message.answer_photo(photo=rdfoto, caption='"Это подпись фотки"')

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    vidos = FSInputFile('s_DR.mp4')
    await bot.send_video(message.chat.id, vidos)

@dp.message(Command('audio'))
async def audio(message: Message):
    zvyk = FSInputFile('8371-mp3.mp3')
    await bot.send_audio(message.chat.id, zvyk)

@dp.message(Command('training'))
async def training(message: Message):
    training_list = ["1. Тренировка 1", "2. Тренировка Два", "3. Тренировка 3"]
    rand_tr = random.choice(training_list)
    await message.answer(f"Это Ваша мини тренировка на  сегодня\n{rand_tr}")

    #Преоброзование тренировки в речевой файл и его отправка
    tts = gTTS(text=rand_tr, lang='ru')
    tts.save('training.ogg')
    audio_tr = FSInputFile('training.ogg')
    await bot.send_voice(message.chat.id, audio_tr)
    os.remove('training.ogg')

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('voice.ogg')
    await message.answer_voice(voice)

@dp.message(Command('doc'))
async def doc(message: Message):
    doce = FSInputFile('ОСАГО.pdf')
    await message.answer_document(doce)

@dp.message(F.photo)
async def answ_foto(message:Message):
    list = ['ОГО крутая ФОТКА', 'Фотка клас', 'Фотка БЭ']
    answ_foto = random.choice(list)
    await message.answer(answ_foto)
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg') # Это строка сохраняет фотку


@dp.message(F.text == "Что такое ИИ") # фильтр в aiogram
async def aitext(message:Message):
    await message.answer('Искусственный интеллект (ИИ, искусственный разум, AI) '
                         '— термин, который означает разработку компьютерных систем, '
                         'способных выполнять задачи, свойственные человеческому интеллекту. '
                         'Это включает анализ данных, распознавание образов, обработку текстов и запросов, '
                         'сформулированных естественным языком, обучение на потоках данных и принятие решений.')


# @dp.message() # отвечает на любые сообщения не описанные в командах
# async def word(message:Message):
#     await message.answer('Ответ на все что не прописанно в Телеботе')

# @dp.message() # эхо бот, отвечает тем что ты ему написал
# async def eho(message:Message):
#     await message.send_copy(chat_id=message.chat.id)

@dp.message() #отлавливает конкретное слово
async def word1(message:Message):
    if message.text.lower() == "жопа":
        await message.answer('Фу, какой ты некультурный')


async def main():
    await dp.start_polling(bot) #Ваш бот использует polling — программа сама "стучится" к Telegram и распределяет сообщения по хендлерам по фильтрам.

if __name__ == '__main__':
    asyncio.run(main())


