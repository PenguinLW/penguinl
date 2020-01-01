from time import sleep;
from telegram import Bot;
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler;
from telegram.ext import MessageHandler;
from telegram.ext import Filters;

from config import P_Bot;

class App():
    def hola_user(app, p_bot: Bot, update: Update):
        content = "";
        if(app.p_inf.search_person(update.message.chat_id) == 0):
            print(update.message.chat_id);
            app.p_inf.add_person(update.message.chat_id);
            content = "Приветсвую!!";
        else:
            content = "Мы уже с Вами знакомы, день добрый!!";
        app.send_answer(
            update.message.chat_id,
            content,
            "markdown"
        );
            
    def answer_user(app, p_bot: Bot, update: Update):
        app.send_answer(
            update.message.chat_id,
            "Рад Вашему слову.",
            "html"
        );
    def send_answer(app, chat_id, text, p_m):
        app.p_bot.send_message(
            chat_id = chat_id,
            text = "*"+text+"*" if p_m == "markdown" else "<em>"+text+"</em>",
            parse_mode = p_m
        );
    def __init__(app):
        app.commande_handler = [];
        app.p_inf = P_Bot();
        app.p_bot = Bot(
            token = app.p_inf.get_token(),
            base_url = app.p_inf.get_base_url()
        );
        app.updater = Updater(bot = app.p_bot);
        
        app.commande_handler.append(CommandHandler("start", app.hola_user));
        app.commande_handler.append(MessageHandler(Filters.text, app.answer_user));
        
        for el in app.commande_handler:
            app.updater.dispatcher.add_handler(el);
        while True:
            app.app_run();
            sleep(240);
    def app_run(app):
        app.updater.start_polling();

if(__name__ == "__main__"):
    App();