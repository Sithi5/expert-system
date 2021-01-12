import argparse
from Resources.Parser.parser import Parser
from Resources.Tree.tree import Tree


def main(file, vb):
    try:
        parser = Parser(file, vb)
        parser.parsing()
        tree = Tree(vb)
        tree.create_all_letternode(parser.rules)
        tree.set_letters_state(parser.rules, parser.facts)
        tree.create_rules_tree()
        tree.rules = parser.rules
        result = "Nothing"
        return result
    except Exception as error:
        return "Error :" + error.args[1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Expert System")
    parser.add_argument("file", type=argparse.FileType("r"), help="The file containing rules")
    parser.add_argument("-vb", "--verbose", action="store_true", help="Enable verbose")
    args = parser.parse_args()
    main(args.file, args.verbose)
