from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data import DATA


__all__ = ['chapters']


def chapters(section_id):
    section = None
    for i in DATA['sections']:
        if i['type'] == section_id:
            section = i
            break
    markup = []
    row = []
    for i in section['section']:
        row.append(KeyboardButton(text=i['title']))
        if len(row) == 2:
            markup.append(row)
            row = []
    markup.append([KeyboardButton(text="Menyuga qaytish")])
    return ReplyKeyboardMarkup(keyboard=markup, resize_keyboard=True, one_time_keyboard=True)
