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
        app.p_base_url = "http://telegg.ru/orig/bot";
        app.dtoken = "7ac8e3b62b22437794a2a4755ada1990";
        app.alph = "abcdefghijklmnopqrstuvwxyz";
        app.l_event = {};

        app.db = P_db();
    
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
    def crear_unplan(app, person_id, tmp):
        """
            Добавление личной рабочей инф пользователя - последующая ..
            notes
            cards
            meeting
            given
            ?
        """
        app.db.connect_to_db();
        tstr = "";
        i = 0;
        for q in tmp:
            tstr += "{0:s} varchar(255), ".format(app.alph[i]);
            app.l_event.update({q: i+1})
            i += 1;
        tstr = tstr[0:-2];
        try:
            app.db.p_user_db.execute("""
                CREATE TABLE _{0:}(
                    row_cnt serial,
                    {1:s}
                );""".format(person_id, tstr)
            );
            i = 0;
            for q in tmp:
                app.db.p_user_db.execute(
                    """
                    INSERT INTO _{0:}
                    ({1:s})
                    VALUES
                    ('{2:s}')
                    """.format(person_id, app.alph[i], "")
                );
                i += 1;
        except:
            app.db.commit_changes_db();
            if(len(tmp) > int(app.db.p_user_db.execute("""
                    select max(row_cnt)
                    from _{0:}
                    """.format(person_id))
            )):
                app.db.p_user_db.execute(
                    """
                    INSERT INTO _{0:}
                    ({1:s})
                    VALUES
                    ({2:n})
                    """.format(person_id, 'row_cnt', len(tmp))
                );
        app.db.commit_changes_db();
        app.db.disconnect_user_db();
    def estab_unplan(app, person_id, tmp):
        """
            .
        """
        app.db.connect_to_db();
        i = 0;
        for q in range(0, len(tmp)-1):
            try:
                app.db.p_user_db.execute(
                    """
                    update _{0:}
                    set {1:s} = '{2:s}'
                    where row_cnt = {3:n}
                    """.format(
                        person_id,
                        app.alph[i],
                        tmp[q],
                        app.l_event[tmp[len(tmp)-1]])
                );
                i += 1;
            except:
                app.db.commit_changes_db();
                app.db.p_user_db.execute(
                    """
                    alter table _{0:}
                    add column {1:s} varchar(255)
                    """.format(
                        person_id,
                        app.alph[i])
                );
                app.db.commit_changes_db();
                app.db.p_user_db.execute(
                    """
                    update _{0:}
                    set {1:s} = '{2:s}'
                    where row_cnt = {3:n}
                    """.format(
                        person_id,
                        app.alph[i],
                        tmp[q],
                        app.l_event[tmp[len(tmp)-1]])
                );
                i += 1;
        app.db.commit_changes_db();
        app.db.disconnect_user_db();
    def get_from(app, person_id, tmp):
        """
            .
        """
        tmp_string = "";
        app.db.connect_to_db();
        app.db.p_user_db.execute(
            """
            select *
            from _{0:}
            where row_cnt = {1:n}
            """.format(person_id, app.l_event[tmp[len(tmp)-1]])
        );
        tmp_string = str(app.db.p_user_db.fetchall())[3:-4]\
            .replace("None", "")\
            .replace("None, ", "")\
            .replace("'', ", "")\
            .replace("', '", "\n")\
            .replace("', ", "")\
            .replace(", '", "\n")[1:];
        app.db.disconnect_user_db();
        return tmp_string;
    
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