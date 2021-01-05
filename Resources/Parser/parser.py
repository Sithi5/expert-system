import re
from Resources.Utils.log import Logger

OPERATORS = "+|^"
logger = Logger("Parser")

OPERATORS = ['!', '+', '|', '^', '(', ')']
PRIORITY = {'^': 0, '|': 1, '+': 2, '!': 3}


class Rule:
	def __init__(self, line, splited_line):
		if line.count("(") != line.count(")"):
			logger.error("Mismatching parantheses")

		self.condition = self.create_rule(splited_line[0])
		self.implication = "<=>" if "<=>" in line else "=>"
		self.result = self.create_rule(splited_line[1])

	def create_rule(self, rule):
		stack = []
		output = ''
		for value in rule:
			if value not in OPERATORS:
				output += value
			elif value == '(':
				stack.append('(')
			elif value == ')':
				while stack and stack[-1] != '(':
					output += stack.pop()
				stack.pop()
			else:
				while stack and stack[-1] != '(' and value != '!' and PRIORITY[value] <= PRIORITY[stack[-1]]:
					output += stack.pop()
				stack.append(value)
		while stack:
			output += stack.pop()
		output = output.replace('!!', '')
		return output

	def __str__(self):
		return f"Conditions : {self.condition:<10}\tImplication : {self.implication:<3}\tResult : {self.result}\n"


class Parser:
	def __init__(self, file):
		self.input = file.readlines()
		self.facts = []
		self.queries = []
		logger.info("Initialization of class")
		self.parsing()

	def parsing(self):
		logger.info("Starting parsing")
		for line in self.input:
			line = line.split("#", 1)[0]
			line = (''.join(line.split()))
			if not line:
				continue
			if line[0] == "=":
				self.fact_parsing(line[1:])
			elif line[0] == "?":
				self.queries_parsing(line[1:])
			else:
				if "=>" not in line and "<=>" not in line:
					logger.error("Rule format incorrect")
				splited_line = re.split("=>|<=>", line)
				rule = Rule(line, splited_line)
				print(rule)

		if len(self.queries) == 0:
			logger.error("No queries")
		if len(self.facts) == 0:
			logger.error("No facts")
		logger.info("End of parsing")

	def fact_parsing(self, line):
		if len(self.facts) != 0:
			logger.error("Facts already defined")
		if line.isalpha() and line.isupper():
			self.facts = list(line)
			logger.info(f"Facts detected : {self.facts}")
		else:
			logger.error("Facts format incorrect")

	def queries_parsing(self, line):
		if len(self.queries) != 0:
			logger.error("Queries already defined")
		if line.isalpha() and line.isupper():
			self.queries = list(line)
			logger.info(f"Queries detected : {self.queries}")
		else:
			logger.error("Queries format incorrect")
