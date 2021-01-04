from Resources.Parser.args import ArgsParser

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
ORANGE = "\033[33m"
BLUE = "\033[34m"
PRUPLE = "\033[35m"
CYAN = "\033[36m"
GREY = "\033[37m"
END = "\033[0m"


class Logger:
	def __init__(self, type):
		self.type = type

	def info(self, message, type=None):
		if ArgsParser.args.verbose:
			type = type or self.type
			print(f"{BLACK}\033[33m<{type}>{END} {message}")
