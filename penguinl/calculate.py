
class Calculate:
    def addition(app, a, b):
        """
            +
        """
        res = a + b;
        return res;
    def subtraction(app, a, b):
        """
            -
        """
        res = a - b;
        return res;
    def multiplication(app, a, b):
        """
            *
        """
        res = a * b;
        return res;
    def division(app, a, b):
        """
            /
        """
        res = a / b;
        return res;
    def remainder_otd(app, a, b):
        """
            %
        """
        res = a % b;
        return res;
    def decimal_to_binary(app, a, b):
        """
            0b
        """
        res = "{0:0b}".format(a);
        return res;
    def decimal_to_octal(app, a, b):
        """
            0o
        """
        res = "{0:0o}".format(a);
        return res;
    def decimal_to_hexadecimal(app, a, b):
        """
            0x
        """
        res = "{0:0x}".format(a);
        return res;
    def __init__(app):
        app.num = [];
        app.do_act = {
            "+": app.addition,
            "-": app.subtraction,
            "*": app.multiplication,
            "/": app.division,
            "%": app.remainder_otd,
            "0b": app.decimal_to_binary,
            "0o": app.decimal_to_octal,
            "0x": app.decimal_to_hexadecimal
        };