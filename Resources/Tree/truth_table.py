from Resources.Utils.log import Logger
from Resources.Tree.node import LetterNode, ConnectorNode, Node

class Truth_table():
	table_and = [[False,False,False],
					[False,True,False],
					[True,False,False],
					[True,True,True],
					[None,False,False],
					[False,None,False],
					[None,True,None],
					[True,None,None],
					[None,None,None]]

	table_or = [[False,False,False],
					[False,True,True],
					[True,False,True],
					[True,True,True],
					[None,True,True],
					[True,None,True],
					[None,False,None],
					[False,None,None],
					[None,None,None]]

	table_xor = [[False,False,False],
					[False,True,True],
					[True,False,True],
					[True,True,False],
					[None,True,None],
					[True,None,None],
					[None,False,None],
					[False,None,None],
					[None,None,None]]

	table_not = [[False,True],
					[True,False],
					[None,None]]

	# table_imply = [[False,False,True],
	# 				[False,True,True],
	# 				[True,False,False],
	# 				[True,True,True]]

	def find_operand_table(self,connector_node):
		if connector_node.type == "+":
			return(self.table_and)
		elif connector_node.type == "|":
			return(self.table_or)
		elif connector_node.type == "^":
			return(self.table_xor)
		else:
			return(self.table_not)
	
	def find_operand_value(self,connector_node,children1_state,children2_state):
		table = self.find_operand_table(connector_node)
		if len(table[0]) == 2:
			for trust in table:
				if children1_state is trust[0]:
					return trust[1]
			return table
		for truth in table:
			if children1_state is truth[0] and children2_state is truth[1]:
				return truth[2]

