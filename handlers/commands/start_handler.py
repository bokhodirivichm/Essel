from loader import dp
from keyboards import LANGUAGES
from aiogram.filters.command import Command
from aiogram.utils.i18n import gettext as _


__all__ = ['start_handler']


@dp.message(Command('start'))
async def start_handler(msg):
    await msg.answer(_('welcome to this bot'))
    await msg.answer(_('can you choose some language'), reply_markup=LANGUAGES)
