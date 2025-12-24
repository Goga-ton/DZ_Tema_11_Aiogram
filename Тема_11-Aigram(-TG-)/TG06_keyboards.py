from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

but_reg =  KeyboardButton(text='Регистрация в TGBot')
but_kyrs_val =  KeyboardButton(text='Курс валют')
but_tips =  KeyboardButton(text='Советы начинающим инвесторам')
but_fin =  KeyboardButton(text='Расходы')

keyboard = ReplyKeyboardMarkup(keyboard=[
    [but_reg,but_kyrs_val],
    [but_tips, but_fin]
], resize_keyboard=True)



# list = ['кнопка-1', 'кнопка-2', 'кнопка-3', 'кнопка-4']
#
# async def list_kb():
#     keyboard = ReplyKeyboardBuilder() # создается пусая клавиатура
#     for key in list:
#         keyboard.add(KeyboardButton(text=key)) #добавляем кнопки
#     return keyboard.adjust(2).as_markup() # в ряду будет 2 кнопки это мы и прописываем, также "as_markup()" это для того чтобы кнопки в телеграм что-то отправляли
#
# list_inv = ['Button-1', 'Button-2', 'Button-3']
#
# async def list_kb_inv():
#     keyboard_inv = InlineKeyboardBuilder() # создается пусая клавиатура
#     for key_inv in list_inv:
#         keyboard_inv.add(InlineKeyboardButton(text=key_inv, url='https://i.pinimg.com/474x/e2/17/b7/e217b73583daf729b12010f7e475acfa.jpg')) #добавляем кнопки
#     return keyboard_inv.adjust(3).as_markup() # в ряду будет 3 кнопки это мы и прописываем, также "as_markup()" это для того чтобы кнопки в телеграм что-то отправляли

