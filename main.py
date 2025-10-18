import asyncio
from aiogram import Bot, Dispatcher
from handler import setup_message_router
from keyboard.default_keyboard import main_keyboard

API_TOKEN = "8157660249:AAHSsWG2HOs_R4sf67_iH3YwSgElCqHSe7U"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def on_startup(dispatcher: Dispatcher):
    await bot.send_message(chat_id="6426538522",
                           text="Bot ishga tushdi")


async def main():
    handler_router = setup_message_router()
    dp.include_router(handler_router)

    await bot.delete_webhook(drop_pending_updates=True)

    await on_startup(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
