import logging
logging.basicConfig(level=logging.DEBUG)
import asyncio
from loader import dp, bot
import handlers


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
