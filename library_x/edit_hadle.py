
from aiogram import Bot, types, Dispatcher, executor
# from dotenv import load_dotenv
import os
import asyncio

#
# load_dotenv()
# p_token = os.getenv("p_token")
# p_admin_id = os.getenv("p_admin_id")


def hola_user(self):
    pass


async def la_calculadora(self):
    pass
async def cr_unplan(self):
    pass
async def el_minutero(self):
    pass
async def show_all_in(app_peng, message: types.Message):
    tmp = message.text.replace("/show_all_in ", "");

    await app_peng.bot.send_message(chat_id=message.chat.id, text=f'Загружаю ваши данные ..')
    # try:
    #     await app_peng.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2);
    #     await app_peng.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1);
    # except:
    #     pass;
    #     await app_peng.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id);

    # await app_peng.bot.send_message(
    #     app_peng.chat_id,
    #     '{:s} ..'.format(
    #         app_peng.p_inf.get_from(message.chat.id, tmp)
    #     )
    # )

    await asyncio.sleep(2)
    await app_peng.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id + 1,
        text='{:s} ..'.format(
            app_peng.p_inf.get_from(message.chat.id, tmp)
        )
    )

    await asyncio.sleep(25)
    await app_peng.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id);

    await app_peng.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id + 1,
        text=f'Удаляю ваши данные ..'
    )

    await asyncio.sleep(11)
    await app_peng.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1);

async def yt_down(self):
    pass