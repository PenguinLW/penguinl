from aiogram import Bot, types, Dispatcher, executor
from dotenv import load_dotenv
import os
import asyncio


from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


from config.config import P_Bot
from library.rock_scissors_paper import rock_scissors_paper
from library_x.edit_handle import *
from library_x.reply_markup import r_kb_m_maker
load_dotenv()
p_token = os.getenv("p_token")
p_admin_id = os.getenv("p_admin_id")

class AppPeng:
    def __init__(self, token):#, chat_id):
        self.bot = Bot(token=token)
        self.dp = Dispatcher(self.bot)
        self.p_admin_id = p_admin_id
        self._setup_handlers()
        self.p_inf = P_Bot();

    def _setup_handlers(self):
        @self.dp.message_handler(commands=['la_comienzo'])
        @self.dp.message_handler(commands=['start'])
        async def handle_start(message: types.Message):
            await self.bot.send_message(message.chat.id, "Бот запущен!")
            await hola_user()

        # @self.dp.message_handler(commands=['la_comienzo'])
        # async def handle_rsp(message: types.Message):
        #     await hola_user()

        @self.dp.message_handler(commands=['la_calculadora'])
        async def handle_la_calculadora(message: types.Message):
            await la_calculadora()

        @self.dp.message_handler(commands=['crearplan'])
        async def handle_crearplan(message: types.Message):
            await cr_unplan()

        @self.dp.message_handler(commands=['el_minutero'])
        async def handle_el_minutero(message: types.Message):
            await el_minutero()

        @self.dp.message_handler(commands=['show_all_in'])
        async def handle_show_all_in(message: types.Message):
            await show_all_in(self, message)

        @self.dp.message_handler(commands=['rsp'])
        async def handle_rsp(message: types.Message):
            await self.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await self.send_and_edit_message(message)

        @self.dp.message_handler(commands=['yt_down'])
        async def handle_yt_down(message: types.Message):
            await yt_down()


        @self.dp.message_handler()
        async def handle_message(message: types.Message):
            await self.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            l_event = self.p_inf.sub_show_plan(message.chat.id)
            # await self.bot.send_message(
            #     message.chat.id,
            #     f"Вы написали: {message.text}",
            #     reply_markup=ReplyKeyboardMarkup([
            #         list(
            #             (KeyboardButton("/show_all_in {0:s}".format(q)) for q in l_event)
            #             if len(l_event) != 0
            #             else [(KeyboardButton("Эй!"))]
            #         )],
            #         resize_keyboard=True, one_time_keyboard=True, selective=True)
            # )
            await self.bot.send_message(
                message.chat.id,
                f"Вы написали: {message.text}",
                # reply_markup=ReplyKeyboardMarkup([
                #     list(
                #         (KeyboardButton("/show_all_in {0:s}".format(q)) for q in l_event)
                #         if len(l_event) != 0
                #         else [(KeyboardButton("Эй!"))]
                #     )],
                #     resize_keyboard=True, one_time_keyboard=True, selective=True)
                reply_markup=r_kb_m_maker(ReplyKeyboardMarkup, KeyboardButton, l_event)
            )
            await asyncio.sleep(25)
            await app_peng.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id+1);

    async def send_and_edit_message(self, message: types.Message):
        message = await self.bot.send_message(chat_id=message.chat.id, text='Ищем игроков ..')

        for i in range(1, 2001):
            content = rock_scissors_paper()
            await asyncio.sleep(2)
            await self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=f'Партия #{i+1}\n{content}')

    def run(self):
        executor.start_polling(self.dp)


app_peng = AppPeng(p_token)#, p_admin_id)
app_peng.run()