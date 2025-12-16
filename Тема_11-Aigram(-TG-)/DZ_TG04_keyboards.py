from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


keyb1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет')], [KeyboardButton(text='Пока')]
], resize_keyboard=True)

keyb1_inl = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Привет', callback_data='hi'),
    InlineKeyboardButton(text='Пока', callback_data='by')]
])

keyb2_inl = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Новости', url='https://www.rbc.ru/politics/15/12/2025/6940355b9a7947258f4e0358?from=from_main_5')],
    [InlineKeyboardButton(text='Музыка', url='https://stock.adobe.com/ru/search/audio?k=1831073401')],
    [InlineKeyboardButton(text='Видео', url='https://media.istockphoto.com/id/2199734931/ru/видео/закат-над-на-море.mp4?s=mp4-640x640-is&k=20&c=uni2RmehBFUuKQ5NlRNM7cBfc7eIVcbYTWADy3SM1LU=')]
])

keyb3_inl = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать больше', callback_data='big')]
])

keyb3_inl2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Опция 1', callback_data='opc1')],
    [InlineKeyboardButton(text='Опция 2', callback_data='opc2')]
])




