from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tests = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📖Matematika'),
            KeyboardButton(text='📚Ona-tili'),
        ],
        [KeyboardButton(text='📐Fizika'),],
        [
            KeyboardButton(text='🌏Geografiya'),
            KeyboardButton(text='🏛Tarix'),
        ]
    ],

    resize_keyboard=True
)