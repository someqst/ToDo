import asyncio
from loader import bot, dp
from handlers import routs_reg
from utils.scheduler import scheduler


async def main():
    dp.include_router(routs_reg())
    scheduler.start()
    await bot.send_message(539937958, 'Старт случился')
    await dp.start_polling(bot)

asyncio.run(main())