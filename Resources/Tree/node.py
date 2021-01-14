from typing import Union


class Node:
    def __init__(self):
        self.children = []
        self.expression_parents = []
        self.result_parents = []
        self.visited = False
        self.state = False
        self.rules_implied_in = []
        self.state_fixed = False
        self.currently_solving = False


class LetterNode(Node):
    def __init__(self, name):
        super(LetterNode, self).__init__()
        self.name = name

    def __repr__(self):
        return f"LetterNode({self.name})"

    def __str__(self):
        return f"LetterNode({self.name})"


class ConnectorNode(Node):
    def __init__(self, op_type: str = None):
        super(ConnectorNode, self).__init__()
        self.type = op_type
        self.state = None


LetterOrConnectorNode = Union[ConnectorNode, LetterNode]
