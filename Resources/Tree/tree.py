from Resources.Utils.log import Logger
from Resources.Tree.node import LetterNode, ConnectorNode, Node

OPERATORS = ["+", "^", "|", "=>", "<=>", "!"]
LST_OP = {"+": "&", "|": "|", "^": "^"}


class Tree:
	_rules = []

	def __init__(self, vb):
		self.vb = vb
		self.logger = Logger("Tree", self.vb)
		self.logger.info("Initialization of class", vb)
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
			table = [[],[],[]]
			for l in rule.expression:
				table[0].append(l)
			table[1].append(rule.implication)
			for l in rule.result:
				table[2].append(l)
			self._rules.append(table)
		if self.vb:
			print()
			print("Setting rules for tree :")
			for idx,rule in enumerate(self.rules):
				print("rule num ",idx," = ", rule)

		
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

	def set_letter_state(self, letter_name, value):
		letter = self.letters.get(letter_name)
		if letter is None:
			self.logger.warning(f"No match found for letter '{letter_name}' in fact section")
			return
		letter.state = value
		if value is True:
			if letter.state_fixed is True:
				self.logger.warning(f"Letter already '{letter_name}' set in fact section before")
			letter.state_fixed = True

	def set_letters_state(self, rules, facts):
		self.logger.info("Setting up states")
		letter_list = self.get_all_letters(rules)
		for letter in letter_list:
			self.set_letter_state(letter, False)
		for fact in facts:
			self.set_letter_state(fact, True)
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

	def print_tree(self):
		root = node
		print("Printing the tree : ")
		while root:
			if isinstance(root, ConnectorNode):
				print(root.type, end=" ")
			elif isinstance(root, LetterNode):
				print(root.name, end="-->")
			root = root.children

	def print_node(self, node):
		if isinstance(node, ConnectorNode):
			print(node.type, end=" ")
		elif isinstance(node, LetterNode):
			print(node.name, end=" ")

	def print_all_parent_from_node(self, node):
		self.print_node(node)
		for parent in node.operand_parents:
			self.print_tree_from_node(parent, print_children=print_children)


	def print_all_children_from_node(self, node: Node, depth=0):
		print(depth, end="")
		self.print_node(node)
		for children in node.children:
			self.print_all_children_from_node(node=children, depth=depth + 1)


	def print_tree_from_implication(self, implication_node):
		print("IMPLICATION TREE :")
		children_one = implication_node.children[0]
		children_two = implication_node.children[1]
		self.print_all_children_from_node(children_one)
		self.print_node(implication_node)
		self.print_all_children_from_node(children_two)

		
	def create_child_tree(self,rule, implication_node):
			stack = []
			for c in rule:
				if c.isupper() and c.isalpha():
					stack.append(self.letters[c])
				else:
					connector_node = ConnectorNode(c, self)
					if c == "!":
						node_children_one = stack.pop()
						node_children_one.operand_parents.append(connector_node)
						connector_node.children.append(node_children_one)
					else:
						node_children_one = stack.pop()
						node_children_two = stack.pop()
						node_children_one.operand_parents.append(connector_node)
						node_children_two.operand_parents.append(connector_node)
						connector_node.children.append(node_children_one)
						connector_node.children.append(node_children_two)
					stack.append(connector_node)
			last_elem = stack.pop()
			last_elem.operand_parents.append(implication_node)
			implication_node.children.append(last_elem)

	def create_rules_tree(self):
		for rule in self.rules:
			print("\n\n\n")
			implication_node = ConnectorNode(rule[1], self)
			# Have to be first !
			self.create_child_tree(rule[0], implication_node)
			self.create_child_tree(rule[2], implication_node)
			self.print_tree_from_implication(implication_node=implication_node)

	def travel_graph_for_letter(self, letter, node):
		# if type(node) == ConnectorNode: // Does this mean anything
		node.visited = True
		for parent in node.operand_parents:
			print("PARENT ",parent.visited , end=" ")
			self.print_node(parent)
			print()
			if parent.visited == False:
				letter.way.append(parent)
				self.travel_graph_for_letter(letter, parent)
		for child in node.children:
			print("CHILD ", child.visited, end=" ")
			self.print_node(child)
			print()
			if child.visited == False:
				letter.way.append(child)
				self.travel_graph_for_letter(letter,child)

	def print_way(self,letter):
		for step in letter.way:
			self.print_node(step)
			






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