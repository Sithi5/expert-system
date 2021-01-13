from Resources.Tree.truth_table import Truth_table
from Resources.Tree.node import LetterNode, ConnectorNode, Node
from Resources.Utils.log import Logger


class QueriesSolver:
    trust_table = Truth_table()

    def __init__(self, vb, queries, tree):
        self.logger = Logger("QueriesSolver", vb)
        self.logger.info("Initialization of class")
        self.queries = queries
        self.tree = tree
        self.solve_queries(queries, tree.letters)

    def get_expression_node_state(self, node) -> bool:
        if isinstance(node, LetterNode):
            return self.solving_letter_state(node)
        elif isinstance(node, ConnectorNode):
            if node.type == "!":
                ret1 = self.get_expression_node_state(node.children[0])
                return self.trust_table.find_operand_value(node, ret1, None)
            else:
                ret1 = self.get_expression_node_state(node.children[0])
                ret2 = self.get_expression_node_state(node.children[1])
                return self.trust_table.find_operand_value(node, ret1, ret2)

    def get_result_node_state(self, node):
        raise NotImplementedError

    def get_implication_state(self, implication_node: ConnectorNode):
        if implication_node.visited is False:
            implication_node.state = self.get_expression_node_state(implication_node.children[0])
            implication_node.visited = True
        return implication_node.state

    def get_letter_state(self, letter_node: LetterNode) -> bool:
        """Return True, False or None depending of the state of the letter,
        respectively for state True, False or undetermined."""
        if letter_node.state is None:
            return None
        elif letter_node.state is True or letter_node.state_fixed is True:
            return True
        else:
            return False

    def solving_letter_state(self, letter_node: LetterNode) -> bool:
        """This method solve the letter state and return it's state"""
        if letter_node.currently_solving is False:
            letter_node.currently_solving = True
            if letter_node.is_solved is not True:
                current_state = self.get_letter_state(letter_node)
                if current_state is not True:
                    for result_parent in letter_node.result_parents:
                        if result_parent.type == "=>":
                            ret = self.get_implication_state(implication_node=result_parent)
                        else:
                            ret = self.get_result_node_state(node=result_parent)
                        if current_state is False or (current_state is None and ret is True):
                            current_state = ret
                letter_node.state = current_state
                letter_node.is_solved = True
            letter_node.currently_solving = False
        return self.get_letter_state(letter_node)

    def solve_queries(self, queries: list, letters: dict):
        """Solve queries for a set of letters_node"""
        for querie in queries:
            for rule in letters[querie].rules_implied_in:
                print("letter : ", querie, " have rule implied in = ", rule)
            self.solving_letter_state(letters[querie])
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
