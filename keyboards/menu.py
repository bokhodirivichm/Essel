from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


__all__ = ['MENU']


MENU = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Bo'lim", callback_data='section'),
        KeyboardButton(text="Modda boyicha qidirish", callback_data='search_by_substance'),
    ],
    [
        KeyboardButton(text="Savol berish", callback_data="ask_question"),
        KeyboardButton(text="Sozlamalar", callback_data="settings"),
    ],
], resize_keyboard=True)

