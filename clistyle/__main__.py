

class Color:
    GREEN = '\033[92m'
    LIGTH_GREEN = '\033[1;92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    BOLD = '\033[;1m'
    CYAN = '\033[1;36m'
    LIGHT_CYAN = '\033[1;96m'
    LIGTH_GREY = '\033[1;37m'
    DARK_GREY = '\033[1;90m'
    BLACK = '\033[1;30m'
    WHITE = '\033[1;97m'
    INVERTE = '\033[;7m'
    RESET = '\033[0m'

    @staticmethod
        def color_decorator(color_code):
            def decorator(func):
                def wrapper(*args, **kwargs):
                    return f"{color_code}{func(*args, **kwargs)}{Color.RESET}"
                return wrapper
            return decorator

    @staticmethod
    def green(func):
        return Color.color_decorator(Color.GREEN)(func)

    @staticmethod
    def light_green(func):
        return Color.color_decorator(Color.LIGTH_GREEN)(func)

    @staticmethod
    def red(func):
        return Color.color_decorator(Color.RED)(func)

    @staticmethod
    def yellow(func):
        return Color.color_decorator(Color.YELLOW)(func)

    @staticmethod
    def blue(func):
        return Color.color_decorator(Color.BLUE)(func)

    @staticmethod
    def magenta(func):
        return Color.color_decorator(Color.MAGENTA)(func)

    @staticmethod
    def bold(func):
        return Color.color_decorator(Color.BOLD)(func)

    @staticmethod
    def cyan(func):
        return Color.color_decorator(Color.CYAN)(func)

    @staticmethod
    def light_cyan(func):
        return Color.color_decorator(Color.LIGHT_CYAN)(func)

    @staticmethod
    def light_grey(func):
        return Color.color_decorator(Color.LIGTH_GREY)(func)

    @staticmethod
    def dark_grey(func):
        return Color.color_decorator(Color.DARK_GREY)(func)

    @staticmethod
    def black(func):
        return Color.color_decorator(Color.BLACK)(func)

    @staticmethod
    def white(func):
        return Color.color_decorator(Color.WHITE)(func)

    @staticmethod
    def inverte(func):
        return Color.color_decorator(Color.INVERTE)(func)
