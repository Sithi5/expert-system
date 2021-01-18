from Resources.Tree.truth_table import Truth_table
from Resources.Tree.node import LetterNode, ConnectorNode, Node, LetterOrConnectorNode
from Resources.Tree.tree_printer import TreePrinter
from Resources.Utils.log import Logger


class QueriesSolver:
    trust_table = Truth_table()
    currently_solving_letters_node = []

    def __init__(self, vb, queries, tree):
        self.vb = vb
        self.tree_printer = TreePrinter(self.vb)
        self.logger = Logger("QueriesSolver", self.vb)
        self.queries = queries
        self.tree = tree
        self.result_operators_functions = {
            "+": self.get_result_and_operator_state,
            "!": self.get_result_not_operator_state,
            "^": self.get_result_xor_operator_state,
            "|": self.get_result_or_operator_state,
            "=>": self.get_implication_state,
        }
        self.result = []

    def get_expression_node_state(self, node: LetterOrConnectorNode) -> bool:
        if isinstance(node, LetterNode):
            # solving_letter_state is setting node.visited to true
            return self.solving_letter_state(node)
        elif isinstance(node, ConnectorNode):
            node.visited = True
            if node.type == "!":
                ret1 = self.get_expression_node_state(node.children[0])
                return self.trust_table.find_operand_value(node, ret1, None)
            else:
                ret1 = self.get_expression_node_state(node.children[0])
                ret2 = self.get_expression_node_state(node.children[1])
                return self.trust_table.find_operand_value(node, ret1, ret2)

    def get_result_and_operator_state(
        self, node: LetterOrConnectorNode, children_node_looking_for_state: LetterOrConnectorNode
    ):
        if node.visited is False:
            node.state = self.get_result_node_state(
                node=node.result_parents[0],
                children_node_looking_for_state=children_node_looking_for_state,
            )
            node.visited = True
        return node.state

    def get_result_not_operator_state(
        self, node: LetterOrConnectorNode, children_node_looking_for_state: LetterOrConnectorNode
    ):
        if node.visited is False:
            ret = self.get_result_node_state(
                node=node.result_parents[0], children_node_looking_for_state=node
            )
            if ret is None:
                node.state = None
            else:
                node.state = not ret
            node.visited = True
        return node.state

    def get_reversed_result_operator_state(
        self, node: LetterOrConnectorNode, children_node_looking_for_state: LetterOrConnectorNode
    ):
        """This method is visiting the result tree from a parent to their childrens to see if
        the current ConnectorNode can be set to true"""
        if isinstance(node, LetterNode):
            return self.solving_letter_state(node)
        if node.children[0] != children_node_looking_for_state:
            other_children_node = node.children[0]
        elif node.children[1] != children_node_looking_for_state:
            other_children_node = node.children[0]
        ret = self.get_reversed_result_operator_state(
            node=other_children_node, children_node_looking_for_state=node
        )
        if isinstance(node, ConnectorNode) and node.type == "!":
            return self.trust_table.find_operand_value(node, ret, None)
        else:
            return self.trust_table.find_operand_value(node, ret, True)

    def get_result_xor_operator_state(
        self, node: LetterOrConnectorNode, children_node_looking_for_state: LetterOrConnectorNode
    ):
        other_children_state = None
        if node.visited is not True:
            # Preventing infinite loop when looking for the other child
            if node.currently_solving is False:
                node.currently_solving = True
                node.state = self.get_result_node_state(
                    node=node.result_parents[0], children_node_looking_for_state=node
                )
                # Getting the other child
                if node.children[0] == children_node_looking_for_state:
                    other_children_node = node.children[1]
                else:
                    other_children_node = node.children[0]
                if isinstance(other_children_node, ConnectorNode):
                    other_children_state = self.get_reversed_result_operator_state(
                        node=other_children_node,
                        children_node_looking_for_state=children_node_looking_for_state,
                    )
                else:
                    other_children_state = self.solving_letter_state(
                        letter_node=other_children_node
                    )

                node.currently_solving = False
                if len(self.currently_solving_letters_node) == 1 or node.state is True:
                    node.visited = True
            else:
                pass
        if node.state is True or node.state is None:
            if other_children_state is True:
                return False
            if node.state is True and other_children_state is False:
                return True
            else:
                return None
        else:
            return False

    def get_result_or_operator_state(
        self, node: LetterOrConnectorNode, children_node_looking_for_state: LetterOrConnectorNode
    ):
        other_children_state_if_not_connector = None
        if node.visited is False:
            # Preventing infinite loop when looking for the other child
            if node.currently_solving is False:
                node.currently_solving = True
                node.state = self.get_result_node_state(
                    node=node.result_parents[0], children_node_looking_for_state=node
                )
                # Getting the other child
                if node.children[0] == children_node_looking_for_state:
                    other_children_node = node.children[1]
                else:
                    other_children_node = node.children[0]
                # If the child is a "not" operator, getting the reverse state result to know if it's true or not
                if isinstance(other_children_node, ConnectorNode) and (
                    other_children_node.type == "!"
                ):
                    other_children_state_if_not_connector = self.get_reversed_result_operator_state(
                        node=other_children_node,
                        children_node_looking_for_state=children_node_looking_for_state,
                    )
                node.currently_solving = False
                if len(self.currently_solving_letters_node) == 1 or node.state is True:
                    node.visited = True
        if node.state is True or node.state is None:
            if other_children_state_if_not_connector is False and node.state is True:
                return True
            else:
                return None
        else:
            return False

    def get_result_node_state(
        self, node: LetterOrConnectorNode, children_node_looking_for_state: LetterOrConnectorNode
    ):
        if isinstance(node, LetterNode):
            self.logger.error("Something is wrong")
        else:
            return self.result_operators_functions[node.type](
                node=node, children_node_looking_for_state=children_node_looking_for_state
            )

    def get_implication_state(self, node: ConnectorNode, *args, **kwargs):
        if node.visited is False:
            node.state = self.get_expression_node_state(node.children[0])
            if len(self.currently_solving_letters_node) == 1 or node.state is True:
                node.visited = True
        return node.state

    def get_letter_state(self, letter_node: LetterNode) -> bool:
        """Only usefull for the state_fixed"""
        if letter_node.state is True or letter_node.state_fixed is True:
            return True
        return letter_node.state

    def solving_letter_state(self, letter_node: LetterNode) -> bool:
        """This method solve the letter state and return it's state"""
        # self.logger.info(f"Solving {letter_node.name}")
        if letter_node.currently_solving is False and letter_node.visited is False:
            self.currently_solving_letters_node.append(letter_node)
            letter_node.currently_solving = True
            current_state = self.get_letter_state(letter_node)
            for result_parent in letter_node.result_parents:
                ret = self.get_result_node_state(
                    node=result_parent, children_node_looking_for_state=letter_node
                )
                if result_parent.type == "!":
                    if letter_node.has_been_updated_to_none_or_true is True:
                        self.logger.error(f"Conflict rules for {letter_node.name}")
                    else:
                        letter_node.has_been_updated_to_false = True
                elif current_state is False or (current_state is None and ret is True):
                    if letter_node.has_been_updated_to_false is True:
                        self.logger.error(f"Conflict rules for {letter_node.name}")
                    else:
                        letter_node.has_been_updated_to_none_or_true = True
                        current_state = ret
            letter_node.state = current_state
            if len(self.currently_solving_letters_node) == 1 or current_state is True:
                letter_node.visited = True
            if len(self.currently_solving_letters_node) != 1:
                self.logger.info(f"We know that {letter_node.name} is {letter_node.state!s:>10}")
            self.currently_solving_letters_node.remove(letter_node)
            letter_node.currently_solving = False
        return self.get_letter_state(letter_node)

    def solve_queries(self):
        """Solve queries for a set of letters_node"""
        self.logger.info("Beginning of the research")
        letters = self.tree.letters
        for querie in self.queries:
            self.logger.info(f"Resolution for letter {letters[querie].name}")
            self.tree_printer.print_rules_implied_in(letters[querie])
            self.solving_letter_state(letters[querie])
            if letters[querie].state is None:
                letters[querie].state = "Undetermined"
            self.result.append(f"{letters[querie].name} is {letters[querie].state}")
            self.logger.info(f"Found '{letters[querie].state}' for {letters[querie].name}")
