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
        app.p_token = "639880775:AAEE5EDh34EBVSpAzHTAF9byK-0lA4Eg0jQ";
        app.p_base_url = "https://api.telegram.org/bot";#"http://telegg.ru/orig/bot";
        app.dtoken = "7ac8e3b62b22437794a2a4755ada1990";

        app.db = P_db();

    #работаем с базой данных "общающихся пользователей"
    def search_person(app, person_id):
        """
            Поиск пользователя - применяется для исключения
            добавления пользователей, уже "начавших общение".
        """
        tmp_string = "";
        try:
            app.db.connect_to_db();
            app.db.p_user_db.execute(
                """
                select count(*)
                from Persons
                where PersonID={0:n};
                """.format(person_id)
            );
            tmp_string = int(app.db.p_user_db.fetchall()[0][0]);
            app.db.disconnect_user_db();
        except:
            app.db.disconnect_user_db();
        return tmp_string;
    def add_person(app, person_id):
        """
            Добавление пользователя - сохранение основной
            информации о пользователе, чтобы исключить в
            последующем "двойное здравствуйте".
        """
        try:
            app.db.connect_to_db();
            app.db.p_user_db.execute(
                """
                insert into Persons
                (PersonID, reg_date, now_date)
                values
                ({0:n}, '{1:s}', {2:s})
                """.format(person_id, app.sub_now(), app.sub_now())
            );
            app.db.commit_changes_db();
            app.db.disconnect_user_db();
        except:
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
        app.sub_create_user(person_id);
        for q in tmp:
            tq = app.sub_count_plan(person_id, q);
            if tq <= 0:
                app.sub_register_plan(person_id, q);
                app.sub_create_plan(person_id, q);
    def estab_unplan(app, person_id, tmp):
        """
            .
        """
        app.sub_delete_plan(person_id, tmp[len(tmp)-1]);
        app.sub_create_plan(person_id, tmp[len(tmp)-1]);
        for q in range(0, len(tmp)-1):
            app.sub_insert_plan(person_id, tmp[len(tmp)-1], tmp[q]);
    def get_from(app, person_id, tmp):
        """
            .
        """
        tmp_string = "";
        try:
            app.db.connect_to_db();
            app.db.p_user_db.execute(
                """
                select *
                from _{1:s}_{0:n}
                """.format(person_id, tmp)
            );
            # tmp_string = str(app.db.p_user_db.fetchall())[3:-4]\
            #     .replace("None", "")\
            #     .replace("None, ", "")\
            #     .replace("'', ", "")\
            #     .replace("', '", "\n")\
            #     .replace("', ", "")\
            #     .replace(", '", "\n")[1:];
            for c in app.db.p_user_db.fetchall():
                tmp_string += "{0:s}\n".format(c[1]);
            app.db.disconnect_user_db();
        except:
            app.db.disconnect_user_db();
        return tmp_string;
    #
    def sub_now(app):
        from datetime import datetime as now;
        nn = str(now.now());#.replace(":", "-");
        return nn;#[:nn.find(".")];
    #
    def sub_create_user(app, person_id):
        """
            .
        """
        try:
            app.db.connect_to_db();
            app.db.p_user_db.execute("""
                create table if not exists _{0:n}(
                    name_of_plan character varying(255),
                    alias_of_plan character varying(255),
                    reg_date timestamp
                );""".format(person_id)
            );
            app.db.commit_changes_db();
            app.db.disconnect_user_db();
        except:
            app.db.commit_changes_db();
            app.db.disconnect_user_db();

    #
    def sub_create_plan(app, person_id, plane_name):
        """
            .
        """
        try:
            app.db.connect_to_db();
            app.db.p_user_db.execute(
                """
                create table if not exists _{1:s}_{0:n}(
                    row_cnt serial,
                    content text,
                    reg_date timestamp
                );""".format(person_id, plane_name)
            );
            app.db.commit_changes_db();
            app.db.disconnect_user_db();
        except:
            app.db.commit_changes_db();
            app.db.disconnect_user_db();
    #
    def sub_register_plan(app, person_id, plane_name):
        """
            .
        """
        try:
            app.db.connect_to_db();
            app.db.p_user_db.execute("""
                insert into _{0:n}
                    (name_of_plan, alias_of_plan, reg_date)
                    values
                    ('{1:s}', '_{1:s}_{0:n}', '{2:s}')
                """.format(person_id, plane_name, app.sub_now())
            );
            app.db.commit_changes_db();
            app.db.disconnect_user_db();
        except:
            app.db.commit_changes_db();
            app.db.disconnect_user_db();
    #
    def sub_insert_plan(app, person_id, plane_name, plane_content):
        """
            .
        """
        try:
            app.db.connect_to_db();
            app.db.p_user_db.execute(
                """
                insert into _{1:s}_{0:n}
                (content, reg_date)
                values
                ('{2:s}', '{3:s}')
                """.format(
                    person_id,
                    plane_name,
                    plane_content,
                    app.sub_now()
            ));
            app.db.commit_changes_db();
            app.db.disconnect_user_db();
        except:
            app.db.commit_changes_db();
            app.db.disconnect_user_db();
    #
    def sub_count_plan(app, person_id, plane_name):
        """
            .
        """
        try:
            app.db.connect_to_db();
            app.db.p_user_db.execute("""
                select count(*)
                from _{0:n}
                where name_of_plan = '{1:s}'
                """.format(person_id, plane_name)
            );
            tmp = int(app.db.p_user_db.fetchall()[0][0])
            app.db.disconnect_user_db();
            return tmp;
        except:
            app.db.disconnect_user_db();
            return 0;
    #
    def sub_show_plan(app, person_id):
        """
            .
        """
        tmp = list();
        try:
            app.db.connect_to_db();
            app.db.p_user_db.execute("""
                select name_of_plan
                from _{0:n}
                """.format(person_id)
            );
            for c in app.db.p_user_db.fetchall():
                tmp.append(c[0]);
            app.db.disconnect_user_db();
            return tmp;
        except:
            app.db.disconnect_user_db();
            return tmp;
    #
    def sub_delete_plan(app, person_id, plane_name):
        try:
            app.db.connect_to_db();
            app.db.p_user_db.execute(
                """
                drop table _{1:s}_{0:n};
                """.format(person_id, plane_name)
            );
            app.db.commit_changes_db();
            app.db.disconnect_user_db();
        except:
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
