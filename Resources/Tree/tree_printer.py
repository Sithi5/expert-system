from Resources.Utils.log import Logger
from Resources.Tree.node import LetterNode, ConnectorNode, Node


class TreePrinter:
    def print_tree(self, node):

        root = node
        print("Printing the tree : ")
        while root:
            if isinstance(root, ConnectorNode):
                print(root.type, end=" ")
            elif isinstance(root, LetterNode):
                print(root.name, end="-->")
            root = root.children

    def print_node(self, node):
        """Printing a node using the type for ConnectorNode or name for LetterNode"""
        if isinstance(node, ConnectorNode):
            print(node.type, end=" ")
        elif isinstance(node, LetterNode):
            print(node.name, end=" ")

    def print_all_parent_from_node(self, node):
        self.print_node(node)
        self.print_all_result_parents_from_node(node=node, print_current_node=False)
        self.print_all_expression_parents_from_node(node=node, print_current_node=False)

    def print_all_result_parents_from_node(self, node, print_current_node=True):
        if print_current_node is True:
            self.print_node(node)
        for parent in node.result_parents:
            self.print_all_result_parents_from_node(node=parent, print_current_node=True)

    def print_all_expression_parents_from_node(self, node, print_current_node=True):
        if print_current_node is True:
            self.print_node(node)
        for parent in node.expression_parents:
            self.print_all_expression_parents_from_node(node=parent, print_current_node=True)

    def print_all_children_from_node(self, node: Node, depth=0):
        print(depth, end="")
        self.print_node(node)
        for children in node.children:
            self.print_all_children_from_node(node=children, depth=depth + 1)

    def print_tree_from_implication(self, implication_node):
        print("\nIMPLICATION TREE :")
        children_one = implication_node.children[0]
        children_two = implication_node.children[1]
        self.print_all_children_from_node(children_one)
        self.print_node(implication_node)
        self.print_all_children_from_node(children_two)

    def travel_graph_for_node(self, start_node, node):
        # if type(node) == ConnectorNode: // Does this mean anything
        node.visited = True
        for parent in node.expression_parents:
            print("PARENT ", parent.visited, end=" ")
            self.print_node(parent)
            print()
            if parent.visited == False:
                start_node.way.append(parent)
                self.travel_graph_for_node(start_node, parent)
        for child in node.children:
            print("CHILD ", child.visited, end=" ")
            self.print_node(child)
            print()
            if child.visited == False:
                start_node.way.append(child)
                self.travel_graph_for_node(start_node, child)

    def print_way(self, node):
        for step in node.way:
            self.tree_printer.print_node(step)
