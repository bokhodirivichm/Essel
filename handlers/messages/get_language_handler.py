from loader import dp
from aiogram import F
from aiogram.utils.i18n import gettext as _
from keyboards import MENU


__all__ = ['get_language']


@dp.message(F.text.lower().in_(['english', 'russian', 'uzbek']))
async def get_language(message):
    await message.answer(_("language changed"))
    await message.answer(_("here is our menu"), reply_markup=MENU)
