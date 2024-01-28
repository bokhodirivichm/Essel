from loader import dp, bot
from aiogram.utils.i18n import gettext as _
from aiogram.utils.chat_action import ChatActionSender
from aiogram import flags
import asyncio


__all__ = ['ask_question_message_handler']


@dp.message()
async def ask_question_message_handler(message):
    async with ChatActionSender(bot=bot, chat_id=message.chat.id):
        await message.answer(_('searching for results please wait.'))
        await asyncio.sleep(5)
        await message.answer(_('no results found'))
