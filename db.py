import psycopg2;
class P_db:

    # выполнение взаимодействия с базой данных пользователей "начавших общение"
    def connect_to_db(app):
        """
            Соединение с базой данных - открытие
            соединия и создание "курсора".
        """
        from dotenv import load_dotenv
        import os

        load_dotenv()

        host = os.getenv("host")
        database = os.getenv("database")
        user = os.getenv("user")
        password = os.getenv("password")
        
        app.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        );
        app.p_user_db = app.conn.cursor();

    def init_db(app):
        """
            Инициализация базы данных - создание таблицы
            с главной информацией об "общающихся
            пользователях" при её отстутствии.
        """
        app.p_user_db.execute("""
            create table if not exists Persons(
                PersonID integer,
                reg_date timestamp,
                now_date timestamp
            );"""
        );
        app.commit_changes_db();

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

    #инициализация экземпляра класса P_db
    def __init__(app):
        """
            .
        """
        app.connect_to_db();
        app.init_db();
        app.disconnect_user_db();
