from aiogram import Bot, Dispatcher
from aiogram.utils.i18n import I18n
from aiogram.utils.i18n.middleware import FSMI18nMiddleware
from aiogram.utils.chat_action import ChatActionMiddleware
import pathlib

TOKEN = "6780158343:AAHKKe7KWkmZphuVCS7FVLvgX0dQmxGoRNA"

bot = Bot(TOKEN, parse_mode='html')
dp = Dispatcher()

i18n = I18n(path="locales", default_locale="en", domain="messages")
i18n_middleware = FSMI18nMiddleware(i18n)
dp.message.middleware(i18n_middleware)
dp.callback_query.middleware(i18n_middleware)

chat_action_middleware = ChatActionMiddleware()
dp.message.middleware(chat_action_middleware)
dp.callback_query.middleware(chat_action_middleware)
