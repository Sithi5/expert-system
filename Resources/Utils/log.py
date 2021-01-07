VERBOSE = True

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
GREY = "\033[37m"
END = "\033[0m"


class Logger:
	def __init__(self, type, vb=False):
		self.type = type
		self.vb = vb

	def info(self, message, type=None):
		if self.vb is True:
			type = type or self.type
			info = f"{YELLOW}<{type}>{END}"
			print(f"{info:24} {message}")

	def warning(self, message, type=None):
		type = type or self.type
		print(f"{PURPLE}<{type}> Warning: {END}{message}")

	def error(self, message, type=None):
		type = type or self.type
		print(f"{RED}<{type}> Error: {END:6}{message}")
		exit()