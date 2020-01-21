from db import P_db;
class P_Bot:
    #инициализация экземпляра класса P_Bot
    def __init__(app):
        """
            Экземпляр класса инициализирует служебные функции,
            необходимые для функционирования приложения, а
            также базовую информацию зарегистрированного
            бота.
        """
        app.p_admin_id = "696236779";
        app.p_token = "639880775:AAFdOtEP2m_1p5ctsB_AAUgE-zb8KSKCUKg";
        app.p_base_url = "https://telegg.ru/orig/bot";
        app.dtoken = "7ac8e3b62b22437794a2a4755ada1990";

        app.db = P_db();
        app.db.connect_to_db();
        app.db.init_db();
        app.db.disconnect_user_db();
    
    #работаем с базой данных "общающихся пользователей"
    def search_person(app, person_id):
        """
            Поиск пользователя - применяется для исключения
            добавления пользователей, уже "начавших общение".
        """
        
        tmp_string = "";
        app.db.connect_to_db();
        app.db.p_user_db.execute(
            """
            SELECT COUNT(*)
            FROM Persons
            WHERE PersonID={0:n};
            """.format(person_id)
        );
        tmp_string = str(app.db.p_user_db.fetchall())[0:-3][2:];
        app.db.disconnect_user_db();
        return int(tmp_string);
    def add_person(app, person_id):
        """
            Добавление пользователя - сохранение основной
            информации о пользователе, чтобы исключить в
            последующем "двойное здравствуйте".
        """
        app.db.connect_to_db();
        app.db.p_user_db.execute(
            """
            INSERT INTO Persons
            (PersonID)
            VALUES
            ({0:n})
            """.format(person_id)
        );
        app.db.commit_changes_db();
        app.db.disconnect_user_db();
    def crear_unplan(app, person_id):
        """
            Добавление личной рабочей инф пользователя - последующая ..
            notes
            cards
            meeting
            given
        """
        app.db.connect_to_db();
        app.db.p_user_db.execute("""
        CREATE TABLE IF NOT EXISTS {0:}(
        row_cnt serial primary_key,
        a varchar(255),
        b varchar(255),
        c varchar(255),
        d varchar(255)
    );
    """.format(person_id));
        app.db.commit_changes_db();
        app.db.disconnect_user_db();
    def estab_unplan(app, person_id):
        """
            .
        """
        app.db.connect_to_db();
        app.db.p_user_db.execute(
            """
            INSERT INTO {0:}
            (a)
            VALUES
            ({1:s})
            """.format(person_id, "+79041239771 сибирский стражник (связь) ")
        );
        app.db.p_user_db.execute(
            """
            INSERT INTO {0:}
            (b)
            VALUES
            ({1:s})
            """.format(person_id, "+79501161160 Софтиум, терешковой 15б-10 (вт 11:30ч.)")
        );
        app.db.p_user_db.execute(
            """
            INSERT INTO {0:}
            (c)
            VALUES
            ({1:s})
            """.format(person_id, "+79140024101 перспектива 24 (вт 14:10ч.)")
        );
        app.db.commit_changes_db();
        app.db.disconnect_user_db();
    
    #получение основной служебной информации для функционирования приложения
    def get_admin_id(app):
        """
            Чат с "создателем", необходимо боту для отчётности о сбоях и пр.
        """
        return app.p_admin_id;
    def get_token(app):
        """
            Токен зарегистрированного бота, необходимо
            для функционирования приложения.
        """
        return app.p_token;
    def get_dtoken(app):
        """
            .
        """
        return app.dtoken;
    def get_base_url(app):
        """
            Ссылка-зеркало для "закрытой РФ".
        """
        return app.p_base_url;