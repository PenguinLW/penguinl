from time import sleep;
from telegram import Bot;
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler;
from telegram.ext import MessageHandler;
from telegram.ext import Filters;

from config import P_Bot;

p_inf = P_Bot();
def hola_user(p_bot: Bot, update: Update):
    p_bot.send_message(
        chat_id=update.message.chat_id,
        text="hola"
    );
def answer_user(p_bot: Bot, update: Update):
    p_bot.send_message(
        chat_id=update.message.chat_id,
        text="answer - {0:n}".format(update.message.chat_id)
    );

def app_run():
    commande_handler = [];
    p_bot = Bot(
        token=p_inf.get_token(),
        base_url=p_inf.get_base_url()
    );
    print(p_inf.get_token(), p_inf.get_base_url());
    updater = Updater(bot=p_bot);
    
    commande_handler.append(CommandHandler("start", hola_user));
    commande_handler.append(MessageHandler(Filters.text, answer_user));
    
    for el in commande_handler:
        updater.dispatcher.add_handler(el);
    while(True):
        updater.start_polling();
        sleep(11400);

if(__name__ == "__main__"):
    app_run();
