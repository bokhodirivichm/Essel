from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
import config
from aiogram.utils.web_app import safe_parse_webapp_init_data
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

import json
import signal
import sys


with open('users_data.json', 'r') as file:
    users_data = json.load(file)

def save_user_language():
    with open('users_data.json', 'w') as file:
        json.dump(users_data, file)

def handle_termination_signal(signal, frame):
    save_user_language()
    sys.exit(0)


with open("languages.json","r", encoding="utf-8") as file:
    languages_data = json.load(file)


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


button_uz = KeyboardButton(languages_data["buttons"]["lang"][0])
button_rus = KeyboardButton(languages_data["buttons"]["lang"][1])



keyboard_lang = ReplyKeyboardMarkup(resize_keyboard=True).add(button_uz,button_rus)




def atvet(id):
    inline_btn_2 = InlineKeyboardButton('Javob qaytarish✉️', callback_data=f'atvet_{id}')
    inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)

    return inline_kb2

ADMINS = [6015129536]

@dp.message_handler(commands=["start", "help"])
async def welcome_upper(message: types.Message):
    users_data[str(message.from_user.id)] = {}
    users_data[str(message.from_user.id)]["lang"] = None
    users_data[str(message.from_user.id)]["state"] = None
    await message.answer(languages_data["choose_lang"], reply_markup=keyboard_lang)

@dp.message_handler()
async def welcome(message: types.Message):
    if message.from_user.id in ADMINS:
        if users_data[str(message.from_user.id)]["state"]!=None:
            if users_data[str(message.from_user.id)]["state"].startswith("help_"):
                help_id = users_data[str(message.from_user.id)]["state"].split("help_")[1]
                await bot.send_message(chat_id = int(help_id), text="Admin: "+message.text)
    elif message.text == languages_data["buttons"]["lang"][0]: #uzb
        users_data[str(message.from_user.id)]["lang"] = "uz"
        button1 = KeyboardButton(languages_data["buttons"]["buy"][users_data[str(message.from_user.id)]["lang"]])
        button2 = KeyboardButton(languages_data["buttons"]["settings"][users_data[str(message.from_user.id)]["lang"]])
        button3 = KeyboardButton(languages_data["buttons"]["help"][users_data[str(message.from_user.id)]["lang"]])
        keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add(button3, button2)
        await message.answer(languages_data["message_1"][users_data[str(message.from_user.id)]["lang"]], reply_markup=keyboard1)

    elif message.text == languages_data["buttons"]["lang"][1]: #rus
        users_data[str(message.from_user.id)]["lang"] = "ru"
        button1 = KeyboardButton(languages_data["buttons"]["buy"][users_data[str(message.from_user.id)]["lang"]])
        button2 = KeyboardButton(languages_data["buttons"]["settings"][users_data[str(message.from_user.id)]["lang"]])
        button3 = KeyboardButton(languages_data["buttons"]["help"][users_data[str(message.from_user.id)]["lang"]])
        keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add(button3, button2)
        await message.answer(languages_data["message_1"][users_data[str(message.from_user.id)]["lang"]], reply_markup=keyboard1)

    elif message.text == languages_data["buttons"]["buy"][users_data[str(message.from_user.id)]["lang"]]: # buy items
        inline_btn_1 = InlineKeyboardButton(languages_data["buttons"]["buy"][users_data[str(message.from_user.id)]["lang"]].lower(),
                                            web_app=types.WebAppInfo(url=f"https://{config.WEBHOOK_HOST+users_data[str(message.from_user.id)]['lang']}"))
        inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

        await bot.send_photo(chat_id=message.chat.id, photo=open(f"menu_{users_data[str(message.from_user.id)]['lang']}.jpg", "rb"),
                             reply_markup=inline_kb1)

    elif message.text == languages_data["buttons"]["settings"][users_data[str(message.from_user.id)]["lang"]]: # settings
        await message.answer(languages_data["choose_lang"], reply_markup=keyboard_lang)

    elif message.text == languages_data["buttons"]["help"][users_data[str(message.from_user.id)]["lang"]]: # help
        button7 = KeyboardButton(languages_data["buttons"]["cancel"][users_data[str(message.from_user.id)]["lang"]])
        keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button7)
        users_data[str(message.from_user.id)]["state"] = "help"
        await message.answer(languages_data["send_message"][users_data[str(message.from_user.id)]["lang"]], reply_markup=keyboard2)

    elif users_data[str(message.from_user.id)]["state"]=="help":
        button1 = KeyboardButton(languages_data["buttons"]["buy"][users_data[str(message.from_user.id)]["lang"]])
        button2 = KeyboardButton(languages_data["buttons"]["settings"][users_data[str(message.from_user.id)]["lang"]])
        button3 = KeyboardButton(languages_data["buttons"]["help"][users_data[str(message.from_user.id)]["lang"]])
        keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add(button3, button2)
        if message.text != languages_data["buttons"]["cancel"][users_data[str(message.from_user.id)]["lang"]]:
            for admin in ADMINS:
                await bot.send_message(chat_id=admin, text=message.text, reply_markup=atvet(message.chat.id))
            await message.answer(text=languages_data["buttons"]["msg_was_sent"][users_data[str(message.from_user.id)]["lang"]], reply_markup=keyboard1)
        else:
            await message.answer(text=languages_data["buttons"]["msg_wasnt_sent"][users_data[str(message.from_user.id)]["lang"]], reply_markup=keyboard1)
        users_data[str(message.from_user.id)]["state"]=None
    


@dp.callback_query_handler()
async def calbackquery(call: types.CallbackQuery):
    chatid = call.data.split("_")[1]
    
    if call.data.startswith("atvet_"):
        await call.message.answer("Xabar jo'nating📩", reply_markup=ReplyKeyboardRemove())
        users_data[str(call.from_user.id)]["state"] = "help_"+chatid


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_termination_signal)
    signal.signal(signal.SIGTERM, handle_termination_signal)
    executor.start_polling(dp)