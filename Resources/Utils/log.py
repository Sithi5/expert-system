from Resources.Utils.colors import YELLOW, PURPLE, RED, END


class Logger:
    def __init__(self, type, vb=False):
        self.type = type
        self.vb = vb

    def info(self, message):
        if self.vb is True:
            info = f"{YELLOW}<{self.type}>{END}"
            print(f"{info:24} {message}")

    def warning(self, message):
        print(f"{PURPLE}<{self.type}> Warning: {END}{message}")

    def error(self, message):
        # type = type or self.type
        print(f"{RED}<{self.type}> Error: {END:6}{message}")
        raise Exception("logger", message)
