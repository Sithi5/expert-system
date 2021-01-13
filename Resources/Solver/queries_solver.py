from Resources.Tree.truth_table import Truth_table
from Resources.Tree.node import LetterNode, ConnectorNode, Node
from Resources.Utils.log import Logger


class QueriesSolver:
    def __init__(self, vb):
        self.logger = Logger("QueriesSolver", vb)
        self.logger.info("Initialization of class")
        self.dict_operators_functions = {
            "=>": self.implication_operator,
            "+": self.and_operator,
            "!": self.no_operator,
            "^": self.xor_operator,
            "|": self.or_operator,
        }

    def implication_operator(self):
        pass

    def and_operator(self):
        # A + B
        # OPERATOR A+B.visited = true
        # if A ! visited : --> solve A
        # if B ! visited : --> solve B
        # RETURN A && B
        pass

    def no_operator(self, node):
        # return not node.children[0].state
        pass

    def xor_operator(self):
        pass

    def or_operator(self):
        pass

    def get_letter_state(self, letter_node: LetterNode) -> bool:
        """Return True, False or None depending of the state of the letter,
        respectively for state True, False or undetermined."""
        if letter_node.state is None:
            return None
        elif letter_node.state is True or letter_node.state_fixed is True:
            return True
        else:
            return False

    def get_state(self, node):
        if isinstance(node, ConnectorNode):
            for child in node.children:
                if child.state is None:
                    return
            node.state = True

    def solving(self, node):
        if isinstance(node, LetterNode):
            print("path: ", node.name, node.state)
        else:
            print("path: ", node.type, node.state)
        self.get_state(node)
        if node.visited is False or node.state is None:
            node.visited = True
            if isinstance(node, LetterNode):
                for parent in node.result_parents:
                    node.state = self.solving(parent)
            if isinstance(node, ConnectorNode):
                for child in node.children:
                    node.state = self.solving(child)
        return node.state

    def solving_from_letter(self, letter_node: LetterNode):
        self.logger.info(f"Letter node = {letter_node} | state = {letter_node.state}")

    def solve_queries(self, queries: list, letters: dict):
        """Solve queries for a set of letters_node"""
        for querie in queries:
            self.solving(letters[querie])
            # self.solving_from_letter(letters[querie])
            print(f"{letters[querie]} is {letters[querie].state}")


# A => B
# =A
# ?B

# def implication_operator(self, implication_node: ConnectorNode) -> bool:
#     ret = self.backtracking_childrens(implication_node.children[0])
#     print("ret implication operator = ", ret)
#     return ret


# def backtracking_parents(self, node) -> bool:
#     self.logger.info(f"In backtracking parents : node = {node}")
#     if len(node.result_parents) > 0:
#         for result_parent in node.result_parents:
#             return self.dict_fun[result_parent.type[0]](implication_node=result_parent)
#     else:
#         return self.get_letter_state(letter_node=node)

# def backtracking_childrens(self, node):
#     if len(node.children) == 0:
#         self.solve_letter(letter_node=node)
#         return self.get_letter_state(letter_node=node)
#     for children in node.children:
#         if isinstance(children, ConnectorNode):
#             self.dict_fun[children.type](implication_node=children)
#         if isinstance(children, LetterNode):
#             self.solve_letter(letter_node=children)
#             return self.get_letter_state(letter_node=children)

# def solve_letter(self, letter_node: LetterNode):
#     self.logger.info(
#         f"Letter node = {letter_node} | state = {letter_node.state} | Letter node state_fixed = {letter_node.state_fixed}"
#     )
#     if self.get_letter_state(letter_node) is True:
#         return
#     else:
#         ret = self.backtracking_parents(letter_node)
#         if ret is None:
#             letter_node.state = None
#         elif ret is True:
#             letter_node.state = True
#         else:
#             letter_node.state = False

# a => B
# on cherche B
# solving(B)
# on arrive sur '=>'
# solving(=>)
# on arrive sur A
# solving de A
# A true
# true => B
# pour que => soi true
# alors B set true
# => set true

# A + B => C
#  on cherche C
#  solving(c)
#  =>
#  solving =>
# on arrive sur +
# solving +
# on arrive sur A
# solving A True
# on arrive sur B
# solving B False
# +
# solving + set + a false
# =>
# false => C donc
