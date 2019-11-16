import psycopg2;
p_token = p_base_url = p_admin_id = "";
class P_Bot:
    def __init__(app):
        global p_token, p_base_url, p_admin_id;
        p_admin_id = "696236779";
        p_token = "639880775:AAFdOtEP2m_1p5ctsB_AAUgE-zb8KSKCUKg";
        p_base_url = "https://telegg.ru/orig/bot";
    def get_admin_id(app):
        global p_admin_id;
        return p_admin_id;
    def get_token(app):
        global p_token;
        return p_token;
    def get_base_url(app):
        global p_base_url;
        return p_base_url;
