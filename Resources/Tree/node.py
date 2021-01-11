class Node:
	way = []
	def __init__(self, tree):
		self.children = []
		self.operand_parents = []
		self.visited = False
		self.state = False
		self.state_fixed = False
		self.tree = tree



class LetterNode(Node):
	def __init__(self, name, tree):
		super(LetterNode, self).__init__(tree)
		self.name = name

	# def __repr__(self):
	# 	return f"LetterNode({self.name})"

	# def __str__(self):
	# 	return f"LetterNode({self.name})"

class ConnectorNode(Node):
	def __init__(self, op_type, tree):
		super(ConnectorNode, self).__init__(tree)
		self.type = op_type
		self.operands = []
		self.state = None
		self.is_root = False