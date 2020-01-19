from telegram import Bot;
from telegram import Update;
from telegram import InlineKeyboardButton;
from telegram import InlineKeyboardMarkup;
from telegram.ext import Updater;
from telegram.ext import CommandHandler;
from telegram.ext import MessageHandler;
from telegram.ext import CallbackQueryHandler;
from telegram.ext import Filters;



import apiai, json, time;

from config import P_Bot;

class App():
    def hola_user(app, p_bot: Bot, update: Update):
        content = "";
        if(app.p_inf.search_person(update.message.chat_id) == 0):
            app.p_inf.add_person(update.message.chat_id);
            content = "Приветствую!!";
            app.send_answer(
                app.p_inf.get_admin_id(),
                "кто-то пришёл: {0:n} сюда: {1:n}".format(update.message.chat_id, update.message.chat_id),
                "markdown"
            );
        else:
            content = "Мы уже с Вами знакомы, день добрый!!";
        app.send_answer(
            update.message.chat_id,
            content,
            "markdown"
        );
            
    def answer_user(app, p_bot: Bot, update: Update):
        req = apiai.ApiAI(app.p_inf.get_dtoken()).text_request();
        req.lang = "ru";
        req.session_id = "PenguinL";
        req.query = update.message.text;

        res = json.loads(req.getresponse().read().decode("utf-8"));
        res = res["result"]["fulfillment"]["speech"];
        if res:
            app.send_answer(
                update.message.chat_id,
                res,
                "html"
            );
        else:
            app.send_answer(
                update.message.chat_id,
                "Рад Вашему слову.",
                "html"
            );

    def help_user(app, p_bot: Bot, update: Update):
        pass;

    def la_calculadora(app, p_bot: Bot, update: Update):
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("1", callback_data='1'),
                    InlineKeyboardButton("2", callback_data='2'),
                    InlineKeyboardButton("3", callback_data='3'),
                    InlineKeyboardButton("4", callback_data='4'),
                    InlineKeyboardButton("5", callback_data='5'),
                    InlineKeyboardButton("6", callback_data='6'),
                    InlineKeyboardButton("7", callback_data='7'),
                    InlineKeyboardButton("8", callback_data='8'),
                    InlineKeyboardButton("9", callback_data='9'),
                    InlineKeyboardButton("0", callback_data='0')],
             [InlineKeyboardButton("+", callback_data='+'),
                    InlineKeyboardButton("-", callback_data='-')],
             [InlineKeyboardButton("=", callback_data='=')]]
        );

        update.message.reply_text('Please choose:', reply_markup=reply_markup);
        app.p_bot.delete_message(update.message.chat_id, update.message.message_id);

    def send_answer(app, chat_id, text, p_m):
        app.p_bot.send_message(
            chat_id = chat_id,
            text = "*"+text+"*" if p_m == "markdown" else "<em>"+text+"</em>",
            parse_mode = p_m
        );
    def button(app, p_bot: Bot, update: Update):
        query = update.callback_query;
        app.calc.append(query.data);
        if(query.data == "="):
            res = 0;
            a = int(app.calc[0]);
            act = app.calc[1];
            b = int(app.calc[2]);
            if(act == "+"):
                res = a + b;
            elif(act == "-"):
                res = a - b;
            query.edit_message_text(res);
            time.sleep(25);
            app.p_bot.delete_message(query.message.chat_id, query.message.message_id);

    def __init__(app):
        app.commande_handler = [];
        app.p_inf = P_Bot();
        app.p_bot = Bot(
            token = app.p_inf.get_token(),
            base_url = app.p_inf.get_base_url()
        );
        app.updater = Updater(bot = app.p_bot);

        app.calc = [];

        app.commande_handler.append(CommandHandler("start", app.hola_user));
        app.commande_handler.append(CommandHandler("la_calculadora", app.la_calculadora));
        app.commande_handler.append(MessageHandler(Filters.text, app.answer_user));
        app.commande_handler.append(CallbackQueryHandler(app.button));
        
        for el in app.commande_handler:
            app.updater.dispatcher.add_handler(el);
        app.app_run();
    def app_run(app):
        app.updater.start_polling();
        app.updater.idle();

if(__name__ == "__main__"):
    App();