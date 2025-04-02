import telegram
from dotenv import load_dotenv
import os
import asyncio # Добавляем asyncio

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

async def send(data): # Делаем функцию асинхронной
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text='Новая информация на сайте! ' + f'{data}') # Добавляем await
    # asyncio.run(main(data)) # Запускаем асинхронную функцию