
class Calculate:
    def addition(app, a, b):
        res = a + b;
        return res;
    def subtraction(app, a, b):
        res = a - b;
        return res;
    def multiplication(app, a, b):
        res = a * b;
        return res;
    def division(app, a, b):
        res = a / b;
        return res;
    def remainder_otd(app, a, b):
        res = a % b;
        return res;
    def __init__(app):
        app.num = [];
        app.do_act = {
            "+": app.addition,
            "-": app.subtraction,
            "*": app.multiplication,
            "/": app.division,
            "%": app.remainder_otd
        };