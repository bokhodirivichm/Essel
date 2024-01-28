from loader import dp
from aiogram import F
from aiogram.utils.i18n import gettext as _
from keyboards import SECTIONS


__all__ = ['result_sections']


@dp.message(F.text.lower() == 'bo\'lim')
async def result_sections(message):
    await message.answer(_("here is sections"), reply_markup=SECTIONS)
