from loader import dp
from aiogram import F
from aiogram.utils.i18n import gettext as _
from data import DATA
from keyboards import MENU


__all__ = ['search', 'search_substance']


ALLOWED_AND_DISALLOWED = """
✅ 47-modda
❌ 47
❌ 47 modda"""

@dp.message(F.text == "Modda boyicha qidirish")
async def search(message):
    await message.answer("<b>Modda nomini yozib qoldiring:</b>\n" + ALLOWED_AND_DISALLOWED)


@dp.message(F.text.contains('-modda'))
async def search_substance(message):
    substance_name = message.text
    res = False
    for a in DATA['sections']:
        for b in a['section']:
            for c in b['section'] if type(b) != str else a['section']['section']:
                if c['title'][0].strip('.') == substance_name:
                    await message.answer(f"<b>{c['title'][0]}</b>\n" + "\n\n".join(
                        ["<i>{}</i>".format(i) for i in c['title'][1:]]
                    ))
                    res = True
    if res:
        await message.answer(_("no results found"))
    
    await message.answer(_("here is our menu"), reply_markup=MENU)
