from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

keyb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Test-1')],
    [KeyboardButton(text='Test-2'), KeyboardButton(text='Test-3')]
], resize_keyboard=True)

keyb_inl = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Серфер', url='https://media.istockphoto.com/id/1140675444/ru/видео/молодой-серфер-копирования-корявый-свою-очередь.mp4?s=mp4-640x640-is&k=20&c=om39h6aJud6xjraOFCfbYI-gXp5UopUcKnLBnINPXe0=')],
    [InlineKeyboardButton(text='Женьщина', url='https://media.istockphoto.com/id/1040315976/ru/фото/женщина-смотрит-на-вид-из-пещеры-матера-базиликата-италия.jpg?s=2048x2048&w=is&k=20&c=C7b9GbZWHqfoflDZqGmXSlqjxfluERr6S-1i2ghztHY=')],
    [InlineKeyboardButton(text='Волна', url='https://media.istockphoto.com/id/2199734931/ru/видео/закат-над-на-море.mp4?s=mp4-640x640-is&k=20&c=uni2RmehBFUuKQ5NlRNM7cBfc7eIVcbYTWADy3SM1LU=')],
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Новости', callback_data='news')],
])

list = ['кнопка-1', 'кнопка-2', 'кнопка-3', 'кнопка-4']

async def list_kb():
    keyboard = ReplyKeyboardBuilder() # создается пусая клавиатура
    for key in list:
        keyboard.add(KeyboardButton(text=key)) #добавляем кнопки
    return keyboard.adjust(2).as_markup() # в ряду будет 2 кнопки это мы и прописываем, также "as_markup()" это для того чтобы кнопки в телеграм что-то отправляли

list_inv = ['Button-1', 'Button-2', 'Button-3']

async def list_kb_inv():
    keyboard_inv = InlineKeyboardBuilder() # создается пусая клавиатура
    for key_inv in list_inv:
        keyboard_inv.add(InlineKeyboardButton(text=key_inv, url='https://i.pinimg.com/474x/e2/17/b7/e217b73583daf729b12010f7e475acfa.jpg')) #добавляем кнопки
    return keyboard_inv.adjust(3).as_markup() # в ряду будет 3 кнопки это мы и прописываем, также "as_markup()" это для того чтобы кнопки в телеграм что-то отправляли



