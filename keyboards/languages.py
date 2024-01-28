from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


__all__ = ['LANGUAGES']


LANGUAGES = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="English"),
        KeyboardButton(text="O'zbek"),
    ],
], resize_keyboard=True)

