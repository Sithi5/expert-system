from Resources.Utils.log import Logger
from Resources.Tree.node import LetterNode, ConnectorNode, Node
from Resources.Tree.tree_printer import TreePrinter

OPERATORS = ["+", "^", "|", "=>", "<=>", "!"]
LST_OP = {"+": "&", "|": "|", "^": "^"}


class Tree:
    _rules = []

    def __init__(self, vb):
        self.vb = vb
        self.logger = Logger("Tree", self.vb)
        self.logger.info("Initialization of class", vb)
        self.tree_printer = TreePrinter()
        self.letters = {}
        self.connectors = []
        self.root_node = None

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, rules: list):
        self._rules = []
        for rule in rules:
            table = [[], [], []]
            for l in rule.expression:
                table[0].append(l)
            table[1].append(rule.implication)
            for l in rule.result:
                table[2].append(l)
            self._rules.append(table)
        if self.vb:
            print()
            print("Setting rules for tree :")
            for idx, rule in enumerate(self.rules):
                print("rule num ", idx, " = ", rule)

    def get_all_letters(self, rules):
        letter_list = []
        for rule in rules:
            for l in rule.expression:
                if l.isalpha() and l.isupper():
                    letter_list.append(l)
            for l in rule.result:
                if l.isalpha() and l.isupper():
                    letter_list.append(l)
        return list(set(letter_list))

    def create_all_letternode(self, rules):
        self.logger.info("Creating LetterNodes")
        letter_list = self.get_all_letters(rules)
        self.letters.update(dict((letter, LetterNode(letter, self)) for letter in letter_list))

    def init_letter_state(self, letter_name, value):
        letter = self.letters.get(letter_name)
        if letter is None:
            self.logger.warning(f"No match found for letter '{letter_name}' in fact section")
            return
        letter.state = value
        if value is True:
            if letter.state_fixed is True:
                self.logger.warning(f"Letter already '{letter_name}' set in fact section before")
            letter.state_fixed = True

    def init_letters_state(self, rules, facts):
        self.logger.info("Setting up states")
        letter_list = self.get_all_letters(rules)
        for letter in letter_list:
            self.init_letter_state(letter, False)
        for fact in facts:
            self.init_letter_state(fact, True)
        self.logger.info("End")

    def create_connector_node(self, rules):
        self.logger.info("create connector node")

    def push_back_node(self, node):
        if self.root_node:
            save_root = self.root_node
            while self.root_node:
                previous = self.root_node
                self.root_node = self.root_node.children
            previous.children = node
            previous.children.children = None
            self.root_node = save_root
        else:
            self.root_node = node
            self.root_node.children = None

    def creating_tree_from_npi_rules(
        self, rule, implication_node, rules_implied_in, is_result=False
    ):
        """Linking node to their parents node.
        rule: input rule with NPI system.
        rules_implied_in: The full rule to add for result node to keep in memory.
        is_result: Set to true to link result_parents to children instead of expression_parents"""
        stack = []
        for c in rule:
            if c.isupper() and c.isalpha():
                stack.append(self.letters[c])
            else:
                connector_node = ConnectorNode(c, self)
                if c == "!":
                    node_children_one = stack.pop()
                    node_children_one.expression_parents.append(connector_node)
                    connector_node.children.append(node_children_one)
                else:
                    # Taking last two elem of stack
                    node_children_one = stack.pop()
                    node_children_two = stack.pop()

                    if is_result:
                        # Keeping the rules implying this parent
                        node_children_one.rules_implied_in.append(rules_implied_in)
                        node_children_two.rules_implied_in.append(rules_implied_in)
                        # Setting connector node as parent of both node
                        node_children_one.result_parents.append(connector_node)
                        node_children_two.result_parents.append(connector_node)
                    else:
                        # Setting connector node as parent of both node
                        node_children_one.expression_parents.append(connector_node)
                        node_children_two.expression_parents.append(connector_node)
                    # Setting both node as child for the connector node
                    connector_node.children.append(node_children_one)
                    connector_node.children.append(node_children_two)
                stack.append(connector_node)
        last_elem = stack.pop()
        if is_result:
            last_elem.result_parents.append(implication_node)
        else:
            last_elem.expression_parents.append(implication_node)
        last_elem.rules_implied_in.append(rules_implied_in)
        implication_node.children.append(last_elem)

    def create_rules_tree(self):
        for rule in self.rules:
            implication_node = ConnectorNode(rule[1], self)
            implication_node.rules_implied_in.append(rule)
            # Have to be first !
            self.creating_tree_from_npi_rules(
                rule[0], implication_node=implication_node, rules_implied_in=rule
            )
            # Creating results tree
            self.creating_tree_from_npi_rules(
                rule[2], implication_node=implication_node, rules_implied_in=rule, is_result=True
            )
            self.tree_printer.print_tree_from_implication(implication_node=implication_node)


# partie de droite test:

# AB|C+ => B

# AB+ => CD|E|

# #
# # partie de droite =
# #

# "C"
# stack = "C"

# "D"
# stack = "CD"

# operator = "|"
# last_two_elem: "CD"
# stack = ""
# operator.children = ["C", "D"]
# stack = "|"

# "E"
# stack = "|E"

# "|"
# last_two_elem: "|E"
# stack = ""
# operator.children = ["|", "E"]
# stack = "|"

# #
# #partie de gauche =
# #

# "A"
# stack = "A"

# "B"
# stack = "AB"

# "+"
# last_two_elem: "AB"
# stack = ""
# operator.children = ["A", "B"]
# stack = "+"


# stack_total = ["+","|"]

# #
# #partie centre =
# #


# implication = "=>"

# 	=>
# 	/\
#   +	  |
# a  b  C D

# tree ->    "|"  -> connectro -> connectro
#          |    |
# 		 A    B
# stack:
# last_two_elem = stack.pop.pop

# [['A', 'C', '+'], ['=>'], ['B', 'G', '|']]
# node | for | -2 create link B --> | link G --> |
