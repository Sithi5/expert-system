from Resources.Utils.log import Logger


logger = Logger("Parser")


class Parser:
	def __init__(self, file):
		self.input = file.readlines()
		self.facts = []
		self.queries = []
		logger.info("Initialization of class")
		self.parsing()

	def parsing(self):
		for line in self.input:
			line = line.split("#", 1)[0]
			line = (' '.join(line.split()))
			if not line:
				continue
			if line[0] == "=":
				pass
			elif line[0] == "?":
				pass
			else:
				pass