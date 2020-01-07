import psycopg2;
class P_Bot:
    #выполнение взаимодействия с базой данных пользователей "начавших общение"
    def connect_to_db(app):
        """
            Соединение с базой данных - открытие
            соединия и создание "курсора".
        """
        app.conn = psycopg2.connect(
            host = "ec2-79-125-4-72.eu-west-1.compute.amazonaws.com",
            database = "d4gh86bmbovta3",
            user = "svnlghwnrdjbdt",
            password = "8684c48054603cb06ee7ea4bc3116909bcb6cd4faaa794891874141914517e20"
        );
        app.p_user_db = app.conn.cursor();
    def init_db(app):
        """
            Инициализация базы данных - создание таблицы
            с главной информацией об "общающихся
            пользователях" при её отстутствии.
        """
        app.p_user_db.execute("""
    CREATE TABLE IF NOT EXISTS Persons(
    PersonID int
);
""");
    def commit_changes_db(app):
        """
            Подтверждение действия в базе данных, такого как,
            например, добавление нового пользователя.
        """
        app.conn.commit();
    def disconnect_user_db(app):
        """
            Закрытие соединения с базой данных и удаление
            "курсора", во избежание "подвешенного 
            подключения" в ожидании происходящего.
        """
        app.p_user_db.close();
        app.conn.close();
        app.p_user_db = "";
        app.conn = "";
    
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
        
        app.connect_to_db();
        app.init_db();
        app.disconnect_user_db();
    
    #работаем с базой данных "общающихся пользователей"
    def search_person(app, person_id):
        """
            Поиск пользователя - применяется для исключения
            добавления пользователей, уже "начавших общение".
        """
        
        tmp_string = "";
        app.connect_to_db();
        app.p_user_db.execute(
            """
            SELECT COUNT(*)
            FROM Persons
            WHERE PersonID={0:n};
            """.format(person_id)
        );
        tmp_string = str(app.p_user_db.fetchall())[0:-3][2:];
        app.disconnect_user_db();
        return int(tmp_string);
    def add_person(app, person_id):
        """
            Добавление пользователя - сохранение основной
            информации о пользователе, чтобы исключить в
            последующем "двойное здравствуйте".
        """
        app.connect_to_db();
        app.p_user_db.execute(
            """
            INSERT INTO Persons
            (PersonID)
            VALUES
            ({0:n})
            """.format(person_id)
        );
        print(person_id);
        app.commit_changes_db();
        app.disconnect_user_db();
    
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