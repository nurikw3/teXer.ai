import asyncio

from aiogram import Bot, Dispatcher, F
from handlers import bot_msg, user_cmds


async def main():
    bot = Bot('7866921848:AAEOBnLHzbniq4JSsmKxQzI5_Dj4ecq4oJA')
    dp = Dispatcher()

    dp.include_routers(
        user_cmds.router,
        bot_msg.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.send_message(1102555863, 'tekser.ai: online')
    await dp.start_polling(bot)


try:

    if __name__ == '__main__':
        asyncio.run(main())
except KeyboardInterrupt:
    exit('stop')