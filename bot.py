import asyncio

from aiogram import Bot, Dispatcher, F
from handlers import bot_msg, user_cmds
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from config_reader import config


async def main():
    bot = Bot(config.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()

    dp.include_routers(
        user_cmds.router,
        bot_msg.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.send_message(1102555863, '*teXser.ai*: online', parse_mode=ParseMode.MARKDOWN)
    await dp.start_polling(bot)

try:
    if __name__ == '__main__':
        asyncio.run(main())
except KeyboardInterrupt:
    exit('stop')