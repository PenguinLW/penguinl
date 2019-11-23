import psycopg2;
from time import sleep;
from telegram import Bot;
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler;
from telegram.ext import MessageHandler;
from telegram.ext import Filters;

from config import P_Bot;

command_handler = p_bot = p_inf = updater = "";
def hola_user(p_bot: Bot, update: Update):
    p_bot.send_message(
        chat_id=update.message.chat_id,
        text="hola"
    );
def answer_user(p_bot: Bot, update: Update):
    p_bot.send_message(
        chat_id=update.message.chat_id,
        text="answer"
    );
class App():
    def __init__(app):
        global command_handler, p_bot, p_inf, updater;
        commande_handler = [];
        p_inf = P_Bot();
        p_bot = Bot(
            token=p_inf.get_token(),
            base_url=p_inf.get_base_url()
        );
        updater = Updater(bot=p_bot);
        
        commande_handler.append(CommandHandler("start", hola_user));
        commande_handler.append(MessageHandler(Filters.text, answer_user));
        
        for el in commande_handler:
            updater.dispatcher.add_handler(el);
    def app_run(app):
        global p_bot, p_inf, updater;
        p_bot.send_message(
            chat_id=p_inf.get_admin_id(),
            text="worked."
        );
        updater.start_polling();

if(__name__ == "__main__"):
    con = psycopg2.connect(
        host = "ec2-79-125-4-72.eu-west-1.compute.amazonaws.com",
        database = "d4gh86bmbovta3",
        user = "postgres",
        password = "postgres"
    );
    app = App();
    app.app_run();
    #while(True):
    #    app.app_run();
    #    sleep(600);#11400);
