from aiogram import Bot, types, Dispatcher, executor
from dotenv import load_dotenv
import os
import asyncio

from library.rock_scissors_paper import rock_scissors_paper
from library.rock_scissors_paper import rock_scissors_paper
from library import rock_scissors_paper
load_dotenv()
p_token = os.getenv("p_token")
p_admin_id = os.getenv("p_admin_id")

class MyBot:
    def __init__(self, token, chat_id):
        self.bot = Bot(token=token)
        self.dp = Dispatcher(self.bot)
        self.chat_id = chat_id
        self._setup_handlers()

    def _setup_handlers(self):
        @self.dp.message_handler(commands=['start'])
        async def handle_start(message: types.Message):
            await self.bot.send_message(message.chat.id, "Бот запущен!")

        @self.dp.message_handler(commands=['rsp'])
        async def handle_rsp(message: types.Message):
            await self.send_and_edit_message()

        @self.dp.message_handler()
        async def handle_message(message: types.Message):
            await self.bot.send_message(message.chat.id, f"Вы написали: {message.text}")

    async def send_and_edit_message(self):
        message = await self.bot.send_message(self.chat_id, 'Начальное сообщение')
        for i in range(5):
            await asyncio.sleep(2)
            await self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=f'Сообщение после обновления {i+1}')

    def run(self):
        executor.start_polling(self.dp)

my_bot = MyBot(p_token, p_admin_id)
my_bot.run()
