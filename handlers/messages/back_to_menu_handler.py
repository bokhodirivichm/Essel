from loader import dp
from aiogram import F
from aiogram.utils.i18n import gettext as _
from keyboards import MENU


__all__ = ['back_to_menu']


@dp.message(F.text == "Menyuga qaytish")
async def back_to_menu(message):
    await message.answer(_("here is our menu"), reply_markup=MENU)
