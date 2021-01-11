import cmd, sys
import re
from Resources.Utils.colors import *

REGEX = re.compile(r"(^((\()*(!){0,2})*[A-Z](\))*(([+|^]((\()*(!){0,2})*[A-Z](\))*)*)?$)")

class Shell(cmd.Cmd):
	intro = "Welcome to the expert-system shell.   Type help or ? to list commands.\n"
	prompt = f"{GREEN}Expert-System{END}:{BLUE}~{END}$ "

	rules = []
	facts = {}
	queries = {}

	def do_add_rule(self, arg):
		"add_rule <rule> : Add a rule"
		if "=>" not in arg and "<=>" not in arg and len(arg) >= 1:
			print("Rule format is incorrect")
		elif len(arg) >= 1:
			arg = arg.replace(" ", "")
			splited_line = re.split("=>|<=>", arg)
			if splited_line[0].count("(") != splited_line[0].count(")") or splited_line[1].count("(") != splited_line[1].count(")"):
				print("Mismatching parantheses in rule")
			if REGEX.match(splited_line[0]) is None or REGEX.match(splited_line[1]) is None:
				print("Rule format is incorrect")
			self.rules.append(arg)
		else:
			print("Rule can't be empty")

	def do_add_fact(self, arg):
		"add_fact <fact(s)> : Add one or more facts"
		if arg.isalpha():
			for letter in arg:
				self.facts.update({letter.upper(): letter.upper()})
		else:
			print("Fact needs to be alphabeticals characters [A-Z]")

	def do_add_querie(self, arg):
		"add_fact <querie(s)> : Add one or more queries"
		if arg.isalpha():
			for letter in arg:
				self.queries.update({letter.upper(): letter.upper()})
		else:
			print("Querie needs to be alphabeticals characters [A-Z]")

	def do_del_rule(self, arg):
		"del_rule <nb> : Delete rule n°<nb>"
		try:
			self.rules.pop(int(arg))
		except Exception:
			if len(self.rules) > 0:
				print(f"Need to be an {GREEN}int{END} in between {YELLOW}0{END} and {YELLOW}{len(self.rules) - 1}{END}")
			else:
				print(f"There is no rule to delete")
		pass

	def do_del_fact(self, arg):
		"del_fact <letter> : Delete fact <letter>"
		try:
			self.facts.pop(arg.upper())
		except Exception:
			if len(arg) == 1 and arg.isalpha():
				print(f"{arg.upper()} not found")
			else:
				print("Fact needs to be an alphabet character [A-Z]")

	def do_del_querie(self, arg):
		"del_querie <letter> : Delete querie <letter>"
		try:
			self.queries.pop(arg.upper())
		except Exception:
			if len(arg) == 1 and arg.isalpha():
				print(f"{arg.upper()} not found")
			else:
				print("Querie needs to be an alphabet character [A-Z]")

	def do_reset_rules(self, arg):
		"reset_rule : Reset all rules"
		self.rules.clear()

	def do_reset_facts(self, arg):
		"reset_facts : Reset all facts"
		self.facts.clear()

	def do_reset_queries(self, arg):
		"reset_queries : Reset all queries"
		self.queries.clear()

	def do_reset_all(self, arg):
		"reset_all : Reset all rules, facts and queries"
		self.do_reset_rules(None)
		self.do_reset_facts(None)
		self.do_reset_queries(None)

	def do_show_all(self, arg):
		"show_all : Show all rules, facts and queries"
		self.do_show_rules(None)
		self.do_show_facts(None)
		self.do_show_queries(None)

	def do_show_rules(self, arg):
		"show_rules : Show rules"
		if len(self.rules) > 0:
			for idx, rule in enumerate(self.rules):
				if arg is not None:
					print(f"Rule n°{idx}: ", end="")
				print(f"{rule}")
		else:
			print("There is no rules to be shown")

	def do_show_facts(self, arg):
		"show_facts : Show facts"
		if len(self.facts) > 0:
			if arg is not None:
				print("Facts:")
			print("=", end="")
			for fact in self.facts:
				print(f"{fact}", end="")
			print()
		else:
			print("There is no facts to be shown")

	def do_show_queries(self, arg):
		"show_queries : Show queries"
		if len(self.queries) > 0:
			if arg is not None:
				print("Queries:")
			print("?", end="")
			for querie in self.queries:
				print(f"{querie}", end="")
			print()
		else:
			print("There is no queries to be shown")

	def do_end(self, arg):
		"Close the shell window, and launch expert-system"
		return True

	def do_exit(self, arg):
		"Close the shell window, and exit"
		exit()
