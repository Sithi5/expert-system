import argparse
import re

from Resources.Utils.log import Logger
from Resources.Parser.parser import Parser, Rule
from Resources.Tree.tree import Tree
from Resources.Tree.truth_table import Truth_table
from Resources.Tree.tree_printer import TreePrinter
from Resources.Solver.queries_solver import QueriesSolver
from Resources.Shell.shell import Shell


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
    parser = Parser(file.readlines(), vb)
    parser.parsing()
    return parser


def tree_solver(parser, vb):
    tree = Tree(vb)
    tree.create_all_letternode(parser.rules, parser.facts, parser.queries)
    tree.init_letters_state(parser.rules, parser.facts, parser.queries)
    tree.rules = parser.rules
    tree.create_rules_tree()
    tree_printer = TreePrinter()
    truth_table = Truth_table()
    solver = QueriesSolver(vb=vb, queries=parser.queries, tree=tree)
    solver.solve_queries()
    return "\n".join(solver.result)


def main_test(file, vb):
    try:
        parser = parsing(file, vb)
        return tree_solver(parser=parser, vb=vb)
    except Exception as error:
        return "Error :" + error.args[1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Expert System")
    parser.add_argument("-vb", "--verbose", action="store_true", help="Enable verbose")
    subparsers = parser.add_subparsers()
    file = subparsers.add_parser("file")
    file.set_defaults(which="file")
    shell = subparsers.add_parser("shell")
    file.add_argument("filename", type=argparse.FileType("r"), help="The file containing rules")
    shell.set_defaults(which="shell")
    args = parser.parse_args()
    try:
        parser = (
            parsing_shell(args.verbose)
            if args.which == "shell"
            else parsing(args.filename, args.verbose)
        )
        print(tree_solver(parser=parser, vb=args.verbose))
    except Exception as error:
        pass
