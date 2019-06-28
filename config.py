p_token = p_base_url = p_admin_id = "";
class P_Bot:
    global p_token, p_base_url, p_admin_id;
    def __init__(app):
        p_admin_id = "696236779";
        p_token = "639880775:AAFdOtEP2m_1p5ctsB_AAUgE-zb8KSKCUKg";
        p_base_url = "https://telegg.ru/orig/bot";
    def get_admin_id(app):
        return p_admin_id;
    def get_token(app):
        return p_token;
    def get_base_url(app):
        return p_base_url;
