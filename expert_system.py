import argparse
import re

from Resources.Utils.log import Logger
from Resources.Parser.parser import Parser, Rule
from Resources.Tree.tree import Tree
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
    """
    Create an instance of class tree
    The class tree create the relation tree between all nodes
    then try to solve each querie in queries list
    """
    tree = Tree(vb, parser.rules)
    tree.create_tree(parser.rules, parser.facts, parser.queries)
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
    subparsers = parser.add_subparsers()
    file = subparsers.add_parser("file")
    file.set_defaults(which="file")
    file.add_argument("-vb", "--verbose", action="store_true", help="Enable verbose")
    file.add_argument("filename", type=argparse.FileType("r"), help="The file containing rules")
    shell = subparsers.add_parser("shell")
    shell.add_argument("-vb", "--verbose", action="store_true", help="Enable verbose")
    shell.set_defaults(which="shell")
    args = parser.parse_args()
    if len(vars(args)) == 0:
        exit("expert_system.py: error: you need too choose between {file,shell}")
    try:
        parser = (
            parsing_shell(args.verbose)
            if args.which == "shell"
            else parsing(args.filename, args.verbose)
        )
        print(tree_solver(parser=parser, vb=args.verbose))
    except Exception as error:
        print(error)
