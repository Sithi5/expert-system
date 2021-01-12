from Resources.Utils.log import Logger
from Resources.Tree.node import LetterNode, ConnectorNode, Node

class Truth_table():
	table_and = [[False,False,False],
					[False,True,False],
					[True,False,False],
					[True,True,True]]

	table_or = [[False,False,False],
					[False,True,True],
					[True,False,True],
					[True,True,True]]

	table_xor = [[False,False,False],
					[False,True,True],
					[True,False,True],
					[True,True,False]]

	table_imply = [[False,False,True],
					[False,True,True],
					[True,False,False],
					[True,True,True]]

	def find_operand_table(self,connector_node):
		if connector_node.type == "+":
			return(self.table_and)
		elif connector_node.type == "|":
			return(self.table_or)
		elif connector_node.type == "^":
			return(self.table_xor)
		else:
			return(self.table_imply)
	
	def find_operand_value(self,connector_node,node1,node2):
		print("\nexpression: ",node1.name,"(",node1.state,")",connector_node.type,node2.name,"(",node2.state,")")
		table = self.find_operand_table(connector_node)
		for truth in table:
			if node1.state == truth[0] and node2.state == truth[1]:
				print("RESULT= ",truth[2])
				return(truth[2])
