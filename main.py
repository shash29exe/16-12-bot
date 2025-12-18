import asyncio
from aiogram import Bot, Dispatcher
import uvicorn

from config import TOKEN
from handlers import h01_start, h02_payments
from webhook.yookassa import app

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(h01_start.router)
dp.include_router(h02_payments.router)

async def start_bot():
    await dp.start_polling(bot)

def start_webhook():
    uvicorn.run(app, host="0.0.0.0", port=8000)

async def main():
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    loop.run_in_executor(None, start_webhook)


if __name__ == '__main__':
    asyncio.run(main())