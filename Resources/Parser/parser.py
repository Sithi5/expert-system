import re

from Resources.Utils.log import Logger

OPERATORS = "+|^"


OPERATORS = ["!", "+", "|", "^", "(", ")"]
PRIORITY = {"^": 0, "|": 1, "+": 2, "!": 3}
REGEX = re.compile(r"(^((\()*(!){0,2})*[A-Z](\))*(([+|^]((\()*(!){0,2})*[A-Z](\))*)*)?$)")


class Rule:
    def __init__(self, line, splited_line, it, vb):
        self.vb = vb
        self.logger = Logger("Parser.Rule", self.vb)
        self.line_nb = it
        self.implication = "=>"
        self.logger.info(
            f"Creation of rule:\t{splited_line[0]} {self.implication} {splited_line[1]}", self.vb
        )
        self.expression = self.check_rule(splited_line[0])
        self.result = self.check_rule(splited_line[1])

    def check_rule(self, string):
        if string.count("(") != string.count(")"):
            self.logger.error("Mismatching parantheses in rule")
        if REGEX.match(string) is None:
            self.logger.error(f"Rule format is incorrect at line {self.line_nb + 1}")
        return self.create_rule(string)

    def create_rule(self, rule):
        stack = []
        output = ""
        for value in rule:
            if value not in OPERATORS:
                output += value
            elif value == "(":
                stack.append("(")
            elif value == ")":
                while stack and stack[-1] != "(":
                    output += stack.pop()
                stack.pop()
            else:
                while (
                    stack
                    and stack[-1] != "("
                    and value != "!"
                    and PRIORITY[value] <= PRIORITY[stack[-1]]
                ):
                    output += stack.pop()
                stack.append(value)
        while stack:
            output += stack.pop()
        output = output.replace("!!", "")
        return output

    def __repr__(self):
        return f"\n{self.expression} {self.implication} {self.result}"

    def __str__(self):
        return f"Conditions : {self.expression:<10}\tImplication : {self.implication:<3}\tResult : {self.result}\n"


class Parser:
    def __init__(self, file, vb):
        self.vb = vb
        self.logger = Logger("Parser.Parser", self.vb)
        self.input = file
        self.facts = []
        self.queries = []
        self.rules = []

    def parsing(self):
        rules_set = 0
        facts_set = 0
        queries_set = 0
        self.logger.info("Starting parsing")
        for it, line in enumerate(self.input):
            line = line.split("#", 1)[0]
            line = "".join(line.split())
            if not line:
                continue
            if line[0] == "=":
                self.fact_parsing(line[1:], facts_set)
                facts_set = 1
            elif line[0] == "?":
                self.queries_parsing(line[1:], queries_set)
                queries_set = 1
            else:
                if "=>" not in line and "<=>" not in line and "<=" not in line:
                    self.logger.error("Rule implication incorrect")
                if rules_set == 0:
                    self.logger.info("Rules detected")
                    rules_set = 1
                splited_line = re.split("=>|<=>|<=", line)
                splited_line = self.deal_with_implication(line, splited_line, it)
                self.rules.append(Rule(line, splited_line, it, self.vb))
        if rules_set == 0:
            self.logger.warning("No rules detected")
        if queries_set == 0:
            self.logger.error("No queries")
        if facts_set == 0:
            self.logger.error("No facts")
        self.logger.info("End of parsing")

    def fact_parsing(self, line, facts_set):
        if facts_set != 0:
            self.logger.error("Facts already defined")
        if len(line) > 0 and line.isalpha() and line.isupper():
            self.facts = list(line)
            self.logger.info(f"Facts detected:\t\t{' '.join(self.facts)}")
        elif len(line) == 0:
            self.facts = []
            self.logger.info(f"Facts detected:\t\t{' '.join(self.facts)}")
        else:
            self.logger.error("Facts format incorrect")

    def queries_parsing(self, line, queries_set):
        if queries_set != 0:
            self.logger.error("Queries already defined")
        if line.isalpha() and line.isupper():
            self.queries = list(line)
            self.logger.info(f"Queries detected:\t{' '.join(self.queries)}")
        else:
            self.logger.error("Queries format incorrect")

    def deal_with_implication(self, line, splited_line, it):
        if "<=>" in line:
            self.rules.append(Rule(line, splited_line, it, self.vb))
            return splited_line[::-1]
        elif "<=" in line:
            return splited_line[::-1]
        elif "=>" in line:
            return splited_line