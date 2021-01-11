import cmd, sys

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
GREY = "\033[37m"
END = "\033[0m"

rules = []
facts = {}
queries = {}

class Shell(cmd.Cmd):
	intro = 'Welcome to the expert-system shell.   Type help or ? to list commands.\n'
	prompt = f"{GREEN}Expert-System{END}:{BLUE}~{END}$ "

	def do_add_rule(self, arg):
		'add_rule <rule> : Add a rule'
		rules.append(arg)

	def do_add_fact(self, arg):
		'add_fact <fact(s)> : Add one or more facts'
		if arg.isalpha():
			for letter in arg:
				facts.update({letter.upper() : letter.upper()})
		else:
			print("Fact needs to be alphabeticals characters [A-Z]")

	def do_add_querie(self, arg):
		'add_fact <querie(s)> : Add one or more queries'
		if arg.isalpha():
			for letter in arg:
				queries.update({letter.upper() : letter.upper()})
		else:
			print("Querie needs to be alphabeticals characters [A-Z]")

	def do_del_rule(self, arg):
		'del_rule <nb> : Delete rule n°<nb>'
		try:
			rules.pop(int(arg))
		except Exception:
			if len(rules) > 0:
				print(f"Need to be an {GREEN}int{END} in between {YELLOW}0{END} and {YELLOW}{len(rules) - 1}{END}")
			else:
				print(f"There is no rule to delete")
		pass

	def do_del_fact(self, arg):
		'del_fact <letter> : Delete fact <letter>'
		try :
			facts.pop(arg.upper())
		except Exception:
			if len(arg) == 1 and arg.isalpha():
				print(f"{arg.upper()} not found")
			else:
				print("Fact needs to be an alphabet character [A-Z]")


	def do_del_querie(self, arg):
		'del_querie <letter> : Delete querie <letter>'
		try :
			queries.pop(arg.upper())
		except Exception:
			if len(arg) == 1 and arg.isalpha():
				print(f"{arg.upper()} not found")
			else:
				print("Querie needs to be an alphabet character [A-Z]")

	def do_reset_rules(self, arg):
		'reset_rule : Reset all rules'
		rules.clear()

	def do_reset_facts(self, arg):
		'reset_facts : Reset all facts'
		facts.clear()

	def do_reset_queries(self, arg):
		'reset_queries : Reset all queries'
		queries.clear()

	def do_reset_all(self, arg):
		'reset_all : Reset all rules, facts and queries'
		self.do_reset_rules(None)
		self.do_reset_facts(None)
		self.do_reset_queries(None)

	def do_show_all(self, arg):
		'show_all : Show all rules, facts and queries'
		self.do_show_rules(None)
		self.do_show_facts(None)
		self.do_show_queries(None)

	def do_show_rules(self, arg):
		'show_rules : Show rules'
		if len(rules) > 0:
			for idx,rule in enumerate(rules):
				if arg is not None:
					print(f"Rule n°{idx}: ", end="")
				print(f"{rule}")
		else:
			print("There is no rules to be shown")

	def do_show_facts(self, arg):
		'show_facts : Show facts'
		if len(facts) > 0:
			if arg is not None:
				print("Facts:")
			print("=", end="")
			for fact in facts:
				print(f"{fact}", end="")
			print()
		else:
			print("There is no facts to be shown")

	def do_show_queries(self, arg):
		'show_queries : Show queries'
		if len(queries) > 0:
			if arg is not None:
				print("Queries:")
			print("?", end="")
			for querie in queries:
				print(f"{querie}", end="")
			print()
		else:
			print("There is no queries to be shown")

	def do_end(self, arg):
		'Close the shell window, and launch expert-system'
		return True

	def do_exit(self, arg):
		'Close the shell window, and exit'
		exit()


if __name__ == '__main__':
	Shell().cmdloop()
	print("Ca continue")