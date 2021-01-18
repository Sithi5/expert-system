import cmd, sys
import numpy as np
import re
import readline
from Resources.Parser.parser import Parser, Rule
from Resources.Tree.tree import Tree
from Resources.Tree.tree_printer import TreePrinter
from Resources.Solver.queries_solver import QueriesSolver
from Resources.Utils.colors import YELLOW, GREEN, BLUE, END

readline.parse_and_bind("tab: complete")

REGEX = re.compile(r"(^((\()*(!){0,2})*[A-Z](\))*(([+|^]((\()*(!){0,2})*[A-Z](\))*)*)?$)")


class Shell(cmd.Cmd):
    intro = "Welcome to the expert-system shell.   Type help or ? to list commands.\n"
    prompt = f"{GREEN}Expert-System{END}:{BLUE}~{END}$ "

    rules = []
    facts = {}
    queries = {}

    def check_rule(self, arg, splited_line):
        if splited_line[0].count("(") != splited_line[0].count(")") or splited_line[1].count(
            "("
        ) != splited_line[1].count(")"):
            print("Mismatching parantheses in rule")
            return
        if REGEX.match(splited_line[0]) is None or REGEX.match(splited_line[1]) is None:
            print("Rule format is incorrect")
            return
        if "<=>" in arg:
            self.rules.append(f"{splited_line[1]}=>{splited_line[0]}")
            self.rules.append(f"{splited_line[0]}=>{splited_line[1]}")
        elif "<=" in arg:
            self.rules.append(f"{splited_line[1]}=>{splited_line[0]}")
        else:
            self.rules.append(arg)

    def do_add_rule(self, arg):
        "add_rule <rule> : Add a rule"
        if "=>" not in arg and "<=>" not in arg and "<=" not in arg and len(arg) >= 1:
            print("Rule format is incorrect")
        elif len(arg) >= 1:
            arg = arg.replace(" ", "")
            splited_line = re.split("=>|<=>|<=", arg)
            self.check_rule(arg, splited_line)

        else:
            print("Rule can't be empty")

    @staticmethod
    def finx_max(list):
        list_len = [len(i) for i in list]
        return np.argmax(np.array(list_len))

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
                print(
                    f"Need to be an {GREEN}int{END} in between {YELLOW}0{END} and {YELLOW}{len(self.rules) - 1}{END}"
                )
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

    def do_load_file(self, arg):
        print(arg)
        with open(arg, "r") as file:
            f = file.readlines()
            for line in f:
                print(line)
                if line[0] == "?":
                    self.do_add_querie(line)
                if line[0] == "=":
                    self.do_add_fact(line)
                else:
                    self.do_add_rule(line)

    def do_save_file(self, arg):
        with open(arg, "w") as file:
            rules = "\n".join(self.rules)
            facts = "=" + "".join(list(self.facts))
            queries = "?" + "".join(list(self.queries))
            content = f"{rules}\n{facts}\n{queries}\n"
            file.write(content)
        print(content)
        print("Saved in :", arg)

    def do_process(self, arg):
        "Solve with expert-system and keep the shell open"
        self.do_show_all(None)
        try:
            parser = Parser(None, True)
            for it, line in enumerate(self.rules):
                splited_line = re.split("=>|<=>", line)
                rule = Rule(line, splited_line, it, True)
                parser.rules.append(rule)
            parser.facts = list(self.facts.keys())
            parser.queries = list(self.queries.keys())
            tree = Tree(True, parser.rules)
            tree.create_tree(parser.rules, parser.facts, parser.queries)
            solver = QueriesSolver(vb=True, queries=parser.queries, tree=tree)
            solver.solve_queries()
            print("\n".join(solver.result))
        except Exception:
            pass

    def do_end(self, arg):
        "Close the shell window, and launch expert-system"
        print(f"Your file :\n{'-' * len(self.rules[self.finx_max(self.rules)])}")
        self.do_show_all(None)
        print(f"{'-' * len(self.rules[self.finx_max(self.rules)])}")
        return True

    def do_exit(self, arg):
        "Close the shell window, and exit"
        exit()
