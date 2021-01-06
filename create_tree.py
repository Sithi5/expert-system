OPERATORS = ["+", "^", "|", "=>", "<=>", "!"]

LST_OP = {'+': "&", '|': "|", '^': '^'}

class Rules:
    def __init__(self, expression, implication, result):
        self.expression = expression
        self.implication = implication
        self.result = result

Rules_list = []
Rules_list.append(Rules("C","=>","E"))
Rules_list.append(Rules("AB+C+","=>","D"))
Rules_list.append(Rules("AB|","=>","C"))
Rules_list.append(Rules("AB!+","=>","F"))
Rules_list.append(Rules("CG!|","=>","H"))
Rules_list.append(Rules("VW^","=>","X"))
Rules_list.append(Rules("AB+","=>","YZ+"))
Rules_list.append(Rules("CD|","=>","XV+"))
Rules_list.append(Rules("EF+","=>","V!"))
Rules_list.append(Rules("AB+","<=>","C"))

class Tree:
    def __init__(self):
        self.letters = {}
        self.connectors = []
        self.rules = []

    def get_all_letters(self, rules):
        for rule in rules:
            letter_list = []
            for l in rule.expression:
                if l.isalpha() and l.isupper():
                    letter_list.append(l)
            print(letter_list)
            self.letters.update(dict((letter, LetterNode(letter, self)) for letter in letter_list))
        print(self.letters)

class Node:
    def __init__(self, tree):
        self.children = []
        self.operand_parents = []
        self.visited = False
        self.tree = tree

class LetterNode(Node):
    def __init__(self, name, tree):
        super(LetterNode, self).__init__(tree)
        self.name = name

    def __repr__(self):
        return f"LetterNode({self.name})"

    def __str__(self):
        return f"LetterNode({self.name})"

class OperatorNode(Node):
    def __init__(self, op_type, tree):
        super(OperatorNode, self).__init__(tree)
        self.type = op_type
        self.operands = []
        self.state = None




tree = Tree()
tree.get_all_letters(Rules_list)
