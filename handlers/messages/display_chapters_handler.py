from loader import dp
from aiogram import F
from aiogram.utils.i18n import gettext as _
from keyboards import chapters


__all__ = ['display_chapters']


@dp.message(F.text.lower().in_(["1-bo'lim", "2-bo'lim", "3-bo'lim", "4-bo'lim", "5-bo'lim", "6-bo'lim"]))
async def display_chapters(message):
    await message.answer(_("here is chapters"),
                         reply_markup=chapters(message.text))
