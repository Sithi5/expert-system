from Resources.Utils.log import Logger
from Resources.Tree.node import LetterNode, ConnectorNode

OPERATORS = ["+", "^", "|", "=>", "<=>", "!"]
LST_OP = {"+": "&", "|": "|", "^": "^"}


class Tree:
	def __init__(self, vb):
		self.vb = vb
		self.logger = Logger("Tree", self.vb)
		self.logger.info("Initialization of class", vb)
		self.letters = {}
		self.connectors = []
		self.rules = []
		self.root_node = ConnectorNode("+", self)
		self.root_node.is_root = True

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
		