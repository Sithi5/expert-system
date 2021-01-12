from Resources.Utils.log import Logger
from Resources.Tree.node import LetterNode, ConnectorNode, Node


def print_tree(node):
    root = node
    print("Printing the tree : ")
    while root:
        if isinstance(root, ConnectorNode):
            print(root.type, end=" ")
        elif isinstance(root, LetterNode):
            print(root.name, end="-->")
        root = root.children


def print_node(node):
    if isinstance(node, ConnectorNode):
        print(node.type, end=" ")
    elif isinstance(node, LetterNode):
        print(node.name, end=" ")


def print_all_parent_from_node(node):
    print_node(node)
    print_all_result_parents_from_node(node=node, print_current_node=False)
    print_all_expression_parents_from_node(node=node, print_current_node=False)


def print_all_result_parents_from_node(node, print_current_node=True):
    if print_current_node is True:
        print_node(node)
    for parent in node.result_parents:
        print_all_result_parents_from_node(node=parent, print_current_node=True)


def print_all_expression_parents_from_node(node, print_current_node=True):
    if print_current_node is True:
        print_node(node)
    for parent in node.expression_parents:
        print_all_expression_parents_from_node(node=parent, print_current_node=True)


def print_all_children_from_node(node: Node, depth=0):
    print(depth, end="")
    print_node(node)
    for children in node.children:
        print_all_children_from_node(node=children, depth=depth + 1)


def print_tree_from_implication(implication_node):
    print("\nIMPLICATION TREE :")
    children_one = implication_node.children[0]
    children_two = implication_node.children[1]
    print_all_children_from_node(children_one)
    print_node(implication_node)
    print_all_children_from_node(children_two)
