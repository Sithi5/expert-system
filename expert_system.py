import argparse
from Resources.Parser.parser import Parser
from Resources.Tree.tree import Tree


def main(file, vb):
	parser = Parser(file, vb)
	tree = Tree(vb)
	tree.create_all_letternode(parser.rules)
	tree.set_letters_state(parser.rules, parser.facts)
	tree.rules = parser.rules
	tree.create_rules_tree()
	###
	print("\n")
	tree.travel_graph_for_letter(tree.letters['G'],tree.letters['G'])
	print("\n")
	tree.print_way(tree.letters['G'])
	###
	result = "Nothing"
	return result


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Expert System")
	parser.add_argument("file", type=argparse.FileType("r"), help="The file containing rules")
	parser.add_argument("-vb", "--verbose", action="store_true", help="Enable verbose")
	args = parser.parse_args()
	main(args.file, args.verbose)
