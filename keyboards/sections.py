from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


__all__ = ['SECTIONS']


SECTIONS = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="1-bo'lim"),
        KeyboardButton(text="2-bo'lim"),
    ],
    [
        KeyboardButton(text="3-bo'lim"),
        KeyboardButton(text="4-bo'lim"),
    ],
    [
        KeyboardButton(text="5-bo'lim"),
        KeyboardButton(text="6-bo'lim"),
    ],
    [
        KeyboardButton(text="Menyuga qaytish")
    ]
], resize_keyboard=True)
