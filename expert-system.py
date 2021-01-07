from Resources.Parser.args import ArgsParser
from Resources.Parser.parser import Parser
from Resources.Tree.tree import Tree

if __name__ == "__main__":
	args = ArgsParser.args
	parser = Parser(args.file)
	tree = Tree()
	tree.create_all_letternode(parser.rules)
	tree.set_letters_state(parser.rules, parser.facts)