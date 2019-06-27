from flask import Flask;
from telegram import Bot;
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler;
from telegram.ext import MessageHandler;
from telegram.ext import Filters;

app = Flask(__name__);
@app.route("/")
@app.route("/index")
def index():
    return "in worked";
def hola_user(p_bot: Bot, update: Update):
    p_bot.send_message(chat_id=update.message.chat_id, text="hola");
def answer_user(p_bot: Bot, update: Update):
    p_bot.send_message(chat_id=update.message.chat_id, text="answer");

def app_run():
    commande_handler = [];
    p_bot = Bot(token="639880775:AAFdOtEP2m_1p5ctsB_AAUgE-zb8KSKCUKg", base_url="https://telegg.ru/orig/bot");
    updater = Updater(bot=p_bot);
    
    commande_handler.append(CommandHandler("start", hola_user));
    commande_handler.append(MessageHandler(Filters.text, answer_user));
    
    for el in commande_handler:
        updater.dispatcher.add_handler(el);
    
    updater.start_polling();

if(__name__ == "__main__"):
    app_run();
    app.run();
