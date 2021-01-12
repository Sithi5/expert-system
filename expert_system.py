import argparse
import re
from Resources.Utils.log import Logger
from Resources.Parser.parser import Parser, Rule
from Resources.Tree.tree import Tree
from Resources.Shell.shell import Shell
import readline

readline.parse_and_bind("tab: complete")


def parsing_shell(vb):
	logger = Logger("Main", vb)
	shell = Shell(completekey="tab")
	shell.cmdloop()
	parser = Parser(None, vb)
	for it, line in enumerate(shell.rules):
		splited_line = re.split("=>|<=>", line)
		rule = Rule(line, splited_line, it, vb)
		parser.rules.append(rule)
	parser.facts = list(shell.facts.keys())
	parser.queries = list(shell.queries.keys())
	if len(parser.queries) == 0:
		logger.error("No queries")
	return parser


def parsing(file, vb):
	# logger = Logger("Main", vb)
	parser = Parser(file.readlines(), vb)
	parser.parsing()
	return parser


def main_test(file, vb):
	try:
		parser = parsing(file, vb)
		tree = Tree(vb)
		tree.create_all_letternode(parser.rules)
		tree.set_letters_state(parser.rules, parser.facts)
		result = "Nothing"
		return result
	except Exception as error:
		return "Error :" + error.args[1]


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Expert System")
	parser.add_argument(
		"-vb", "--verbose", action="store_true", help="Enable verbose"
	)
	subparsers = parser.add_subparsers()
	file = subparsers.add_parser("file")
	file.set_defaults(which="file")
	shell = subparsers.add_parser("shell")
	file.add_argument(
		"filename",
		type=argparse.FileType("r"),
		help="The file containing rules",
	)
	shell.set_defaults(which="shell")
	args = parser.parse_args()
	try:
		parser = (
			parsing_shell(args.verbose)
			if args.which == "shell"
			else parsing(args.filename, args.verbose)
		)
		tree = Tree(args.verbose)
		tree.create_all_letternode(parser.rules)
		tree.set_letters_state(parser.rules, parser.facts)
	except Exception as error:
		pass
