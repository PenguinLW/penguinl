from telegram import Update;
from telegram import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup;
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, CallbackQueryHandler, Filters;
import asyncio

from library import calculate as calc
from config import config
from data import db
from library import calculate, rock_scissors_paper
#from penguinl_x import penguinl_x
# from library_x.reply_markup import r_kb_m_maker
import os, time;  # apiai,

from config.config import P_Bot;


class App():
    def hola_user(app, update: Update, context: CallbackContext):
        if app.p_inf.search_person(update.message.chat_id) == 0:
            app.p_inf.add_person(update.message.chat_id);
            content = "Приветствую!!";
            app.send_answer(
                update,
                context,
                app.p_inf.get_admin_id(),
                "кто-то пришёл: {0:n} сюда: {1:n}".format(update.message.chat_id, update.message.chat_id),
                "markdown"
            );
        else:
            content = "Мы уже с Вами знакомы, день добрый!!";
        context.bot.delete_message(update.message.chat_id, update.message.message_id);
        app.send_answer(
            update,
            context,
            update.message.chat_id,
            content,
            "markdown"
        );

    #
    def help_user(app, update: Update, context: CallbackContext):
        pass;

    #
    def la_calculadora(app, update: Update, context: CallbackContext):
        c = app.c;
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("1", callback_data=1),
              InlineKeyboardButton("2", callback_data=2),
              InlineKeyboardButton("3", callback_data=3),
              InlineKeyboardButton("4", callback_data=4)],
             [InlineKeyboardButton("5", callback_data=5),
              InlineKeyboardButton("6", callback_data=6),
              InlineKeyboardButton("7", callback_data=7),
              InlineKeyboardButton("8", callback_data=8)],
             [InlineKeyboardButton("9", callback_data=9),
              InlineKeyboardButton("0", callback_data=0),
              InlineKeyboardButton(".", callback_data="."),
              InlineKeyboardButton("bin", callback_data="0b"),
              InlineKeyboardButton("oct", callback_data="0o"),
              InlineKeyboardButton("hex", callback_data="0x")],
             [InlineKeyboardButton("+", callback_data='+'),
              InlineKeyboardButton("-", callback_data='-'),
              InlineKeyboardButton("*", callback_data='*'),
              InlineKeyboardButton("/", callback_data='/'),
              InlineKeyboardButton("%", callback_data='%')],
             [InlineKeyboardButton("=", callback_data='=')]]
        );

        update.message.reply_text('Please choose:', reply_markup=reply_markup);
        context.bot.delete_message(update.message.chat_id, update.message.message_id);

    def calc_b(app, update: Update, context: CallbackContext):
        c = app.c;
        query = update.callback_query;
        try:
            if query.data.find(".") != -1:
                app.f_flag = True;
                if len(c.num) == 1:
                    c.num[0] = float(c.num[0]);
                elif len(c.num) == 3:
                    c.num[2] = float(c.num[2]);
            elif app.f_flag:
                if len(c.num) == 1:
                    c.num[0] = float(
                        str(c.num[0]).replace(".0", ".") + query.data
                        if
                        str(c.num[0]).find(".0") != -1
                        else
                        str(c.num[0]) + query.data
                    );
                elif len(c.num) == 3:
                    c.num[2] = float(
                        str(c.num[2]).replace(".0", ".") + query.data
                        if
                        str(c.num[2]).find(".0") != -1
                        else
                        str(c.num[2]) + query.data
                    );
            else:
                c.num.append(int(query.data));
                if len(c.num) == 2:
                    c.num[0] = int(str(c.num[0]) + query.data);
                    c.num.remove(c.num[1]);
                elif len(c.num) > 3:
                    c.num[2] = int(str(c.num[2]) + query.data);
                    c.num.remove(c.num[3]);
        except:
            app.f_flag = False;
            c.num.append(query.data);
        if query.data == '=':
            res = 0;
            a = c.num[0];
            act = c.num[1];
            b = c.num[2];

            res = c.do_act[act](a, b);
            c.num = [];
            time.sleep(25);
            query.edit_message_text(res);
            app.f_flag = False;
            time.sleep(25);
            context.bot.delete_message(query.message.chat_id, query.message.message_id);

    #
    def cr_unplan(app, update: Update, context: CallbackContext):
        tmp = update.message.text.replace("/crearplan ", "").split(" ");
        app.p_inf.crear_unplan(update.message.chat_id, tmp);
        context.bot.delete_message(update.message.chat_id, update.message.message_id);

    def el_minutero(app, update: Update, context: CallbackContext):
        tmp = update.message.text.replace("/el_minutero ", "").split("\n");
        app.p_inf.estab_unplan(update.message.chat_id, tmp);
        context.bot.delete_message(update.message.chat_id, update.message.message_id);

    def show_all_in(app, update: Update, context: CallbackContext):
        tmp = update.message.text.replace("/show_all_in ", "");
        try:
            context.bot.delete_message(update.message.chat_id, update.message.message_id - 2);
            context.bot.delete_message(update.message.chat_id, update.message.message_id - 1);
        except:
            pass;
        context.bot.delete_message(update.message.chat_id, update.message.message_id);
        app.send_answer(
            update,
            context,
            update.message.chat_id,
            app.p_inf.get_from(update.message.chat_id, tmp),
            "html"
        );
        time.sleep(25);
        context.bot.delete_message(update.message.chat_id, update.message.message_id + 1);
    
    def rsp_wrapper(app, update: Update, context: CallbackContext):
        from ..library.rock_scissors_paper import rock_scissors_paper
        
        context.bot.delete_message(update.message.chat_id, update.message.message_id);
        content = rock_scissors_paper()
        '''app.send_answer(
            update,
            context,
            update.effective_chat.id,
            "Ищем игроков ..",
            "markdown"
        );'''
        for i in range(1, 2001):
            content = rock_scissors_paper()
            app.send_answer(
                update,
                context,
                update.message.chat_id,
                "{:s}{:n}.\n{:s}".format("Партия №", i, content),
                "markdown"
            );
            '''
            context.bot.edit_message_text(
                update.effective_chat.id,#update.effective_chat.id,#update.message.chat_id,
                update.message.message_id,#update.message.message_id + 1,
                content
            );
            '''
            time.sleep(50);#await asyncio.sleep(50);
            context.bot.delete_message(update.message.chat_id, update.message.message_id + i);
    
    def yt_down(app, update: Update, context: CallbackContext):
        link = update.message.text.replace("/yt_down ", "");
        qlt = True if link.find('qlt') != -1 else False;
        link = link[:len(link) - 4] if link.find('qlt') != -1 else link;
        yt = '';
        vd_name = '';
        vd_file = '';

        from pytube import YouTube;

        #         try:
        #         except:
        #             pass;

        try:
            # YouTube(tmp).streams.first().download();
            yt = YouTube(link);

            vd_name = yt.streams.filter(
                progressive=True,
                file_extension='mp4'
            ).order_by('resolution').desc().first().title;
            vd_file = yt.streams.filter(
                progressive=True,
                file_extension='mp4'
            ).order_by('resolution').desc().first().default_filename;
            context.bot.delete_message(update.message.chat_id, update.message.message_id);

            app.send_answer(
                update,
                context,
                update.message.chat_id,
                'down init: {0:}'.format(vd_name),
                "html"
            );
            if not qlt:
                yt.streams.filter(
                    progressive=True,
                    file_extension='mp4'
                ).order_by('resolution').desc().first().download();
            else:
                yt.streams.filter(
                    progressive=True,
                    file_extension='mp4'
                ).order_by('resolution').desc().last().download();

            #            app.edit_answer(
            #                update,
            #                context,
            #                update.message.chat_id,
            #                update.message.message_id+1,
            #                'down completed: {0:}\njst send..'.format(tmp),
            #                "html"
            #            );
            context.bot.delete_message(update.message.chat_id, update.message.message_id + 1);
            app.send_answer(
                update,
                context,
                update.message.chat_id,
                'down completed: {0:}\njst send..'.format(vd_file),
                "html"
            );
            #            app.edit_media(
            #                update,
            #                context,
            #                update.message.chat_id,
            #                update.message.message_id+1,
            #                tmp
            #            );
            context.bot.delete_message(update.message.chat_id, update.message.message_id + 2);
            app.send_doc(
                update,
                context,
                update.message.chat_id,
                vd_file,
                vd_name
            );
        except:
            app.send_answer(
                update,
                context,
                update.message.chat_id,
                'down stopped: {0:}.'.format(vd_name),
                "html"
            );
            time.sleep(4);
            try:
                context.bot.delete_message(update.message.chat_id, update.message.message_id + 3);
            except:
                context.bot.delete_message(update.message.chat_id, update.message.message_id);
                context.bot.delete_message(update.message.chat_id, update.message.message_id + 1);

    #
    def answer_user(app, update: Update, context: CallbackContext):
        # req = apiai.ApiAI(app.p_inf.get_dtoken()).text_request();
        # req.lang = "ru";
        # req.session_id = "PenguinL";
        # req.query = update.message.text;
        #
        # res = json.loads(req.getresponse().read().decode("utf-8"));
        # res = res["result"]["fulfillment"]["speech"];
        res = False
        if res:
            app.send_answer(
                update,
                context,
                update.message.chat_id,
                res,
                "html"
            );
        else:
            app.send_answer(
                update,
                context,
                update.message.chat_id,
                "Рад Вашему слову.",
                "html"
            );

    #
    def send_answer(app, update, context, chat_id, text, p_m):
        if app.p_inf.search_person(update.message.chat_id) != 0:
            l_event = app.p_inf.sub_show_plan(chat_id);
            time.sleep(4);
            context.bot.send_message(
                chat_id=chat_id,
                text="*" + text + "*" if p_m == "markdown" else "<em>" + text + "</em>",
                parse_mode=p_m,
                # reply_markup=r_kb_m_maker(ReplyKeyboardMarkup, KeyboardButton, l_event)
                reply_markup=ReplyKeyboardMarkup([
                    list(
                        (KeyboardButton("/show_all_in {0:s}".format(q)) for q in l_event)
                        if len(l_event) != 0
                        else [(KeyboardButton("Эй!"))]
                    )],
                    resize_keyboard=True, one_time_keyboard=True, selective=True)
            );
        else:
            context.bot.delete_message(update.message.chat_id, update.message.message_id);
            text = "Вы не зарегистрированы в системе." + \
                   "Используйте /start для того, чтобы начать наше продуктивное общение.";
            p_m = "html"
            time.sleep(4);
            context.bot.send_message(
                chat_id=chat_id,
                text="*" + text + "*" if p_m == "markdown" else "<em>" + text + "</em>",
                parse_mode=p_m
            );
            time.sleep(4);
            context.bot.delete_message(update.message.chat_id, update.message.message_id + 1);

    #     def edit_answer(app, update, context, chat_id, message_id, text, p_m):
    #             contex.bot.edit_message_text(chat_id=message.chat_id,
    #                   message_id=message.message_id,
    #                   *args,
    #                   **kwargs);
    #             time.sleep(25);
    #             context.bot.edit_message_text(
    #                 chat_id = chat_id,
    #                 message_id = message_id,
    #                 text = "*"+text+"*" if p_m == "markdown" else "<em>"+text+"</em>",
    #                 parse_mode = p_m
    #             );
    #     def edit_media(app, update, context, chat_id, message_id, m_media):
    #             contex.bot.edit_message_media(chat_id=message.chat_id,
    #                    message_id=message.message_id,
    #                    *args,
    #                    **kwargs)
    #             from telegram import InputMediaVideo;
    #             time.sleep(25);
    #             context.bot.edit_message_media(
    #                 chat_id = chat_id,
    #                 message_id = message_id
    #                 media = InputMediaVideo(media = m_media)
    #             );
    def send_doc(app, update, context, chat_id, doc, doc_name='..'):
        time.sleep(4);
        context.bot.send_document(
            chat_id=chat_id,
            document=open(doc, 'rb'),
            disable_content_type_detection=False,
            caption=doc_name
        );
        if os.path.exists(doc):
            os.remove(doc);

    #
    def __init__(app):
        app.commande_handler = [];
        app.p_inf = P_Bot();
        app.updater = Updater(
            token=app.p_inf.get_token(),
            base_url=app.p_inf.get_base_url(),
            use_context=True
        );
        
        app.c = calc.Calculate();
        app.f_flag = False;

        app.commande_handler.append(CommandHandler("start", app.hola_user));
        app.commande_handler.append(CommandHandler("la_comienzo", app.hola_user));
        app.commande_handler.append(CommandHandler("la_calculadora", app.la_calculadora));
        app.commande_handler.append(CommandHandler("crearplan", app.cr_unplan));
        app.commande_handler.append(CommandHandler("el_minutero", app.el_minutero));
        app.commande_handler.append(CommandHandler("show_all_in", app.show_all_in));
        app.commande_handler.append(CommandHandler("rsp", app.rsp_wrapper));
        app.commande_handler.append(CommandHandler("yt_down", app.yt_down));
        app.commande_handler.append(MessageHandler(Filters.text, app.answer_user));
        app.commande_handler.append(CallbackQueryHandler(app.calc_b));

        for el in app.commande_handler:
            app.updater.dispatcher.add_handler(el);
        app.app_run();
    
    async def ausp(app):
        app.updater.start_polling()
    
    def app_run(app):
        #app.updater.start_polling();
        
        #asyncio.run(app.ausp())
        loop = asyncio.new_event_loop()  # Создаем новый цикл событий
        asyncio.set_event_loop(loop)  # Устанавливаем его текущим
        loop.run_until_complete(app.ausp())  # Запускаем асинхронную функцию
        loop.close()
        
        # if app.f_flag:
        #    app.updater.start_polling();
        # else:
        #    # add handlers
        #    app.updater.start_webhook(
        #        listen = "0.0.0.0",
        #        port = int(os.environ.get('PORT', '8443')),
        #        url_path = app.p_inf.get_token()#,
        #        #webhook_url = app.p_inf.get_webhook_host() + app.p_inf.get_token()
        #        #url_path = app.p_inf.get_token()
        #    );
        #    #app.updater.bot.set_webhook("https://penguinl.herokuapp.com/" + app.p_inf.get_token());
        # add handlers
        app.updater.start_webhook(
            listen="0.0.0.0",
            port=int(os.environ.get('PORT', '8443')),
            url_path=app.p_inf.get_token()  # ,
            # webhook_url = app.p_inf.get_webhook_host() + app.p_inf.get_token()
            # url_path = app.p_inf.get_token()
        );
        # app.updater.bot.set_webhook("https://penguinl.herokuapp.com/" + app.p_inf.get_token());

        #app.updater.idle();


if __name__ == "__main__":
    App();
