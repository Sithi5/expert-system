"""
C => E # C implies E
(A + B) + C => D # A and B and C implies D
A | B => C # A or B implies C
A + !B => F # A and not B implies F
C | !G => H # C or not G implies H
V ^ W => X # V xor W implies X
A + B => Y + Z # A and B implies Y and Z
C | D => X + V # C or D implies X or V
E + F => !V # E and F implies not V
A + B <=> C # A and B if and only if C
A + B <=> !C # A and B if and only if not C

=ABG # Initial facts : A, B and G are true. All others are false.
# If no facts are initially true, then a simple "=" followed
# by a newline is used

?GVX # Queries : What are G, V and X ?
"""

class Rules:
    def __init__(self, expression, implication, result):
        self.expression = expression
        self.implication = implication
        self.result = result

class Fact_Node:
    tree = []
    def __init__(self, letter, true, false, related_letter):
        self.letter =letter
        self.true = true
        self.flase = false
        self.related_letter = related_letter

class Query:
    def __init__(self, query):
        self.letter = query
        self.query_list = []
        for x in query:
            self.query_list.append(Fact_Node(x,False,False,[]))

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
# Rules_list.append(Rules("AB+","<=>","C!"))

Query_list = Query(['G', 'V', 'X'])

Facts_list = []
Facts_list.append(Fact_Node("A",True,False,[]))
Facts_list.append(Fact_Node("B",True,False,[]))
Facts_list.append(Fact_Node("C",False,True,[]))
Facts_list.append(Fact_Node("D",False,True,[]))
Facts_list.append(Fact_Node("E",False,True,[]))
Facts_list.append(Fact_Node("F",False,True,[]))
Facts_list.append(Fact_Node("G",True,False,[]))
Facts_list.append(Fact_Node("H",False,True,[]))
Facts_list.append(Fact_Node("V",False,True,[]))
Facts_list.append(Fact_Node("W",False,True,[]))
Facts_list.append(Fact_Node("X",False,True,[]))
Facts_list.append(Fact_Node("Y",False,True,[]))
Facts_list.append(Fact_Node("Z",False,True,[]))


def rule_dissec(rule, fact):
    addletter = 0
    for l in rule.expression:
        if l.isalpha() and l.isupper():
            if l not in fact.related_letter and l != fact.letter:
                addletter += 1
                print ("LETTER: " + l)
                fact.related_letter.append(l)
    for l in rule.result:
        if l.isalpha() and l.isupper():
            if l not in fact.related_letter and l != fact.letter:
                addletter += 1
                print ("LETTER: " + l)
                fact.related_letter.append(l)
    if addletter != 0:
        print("RULES:",rule.expression,rule.implication, rule.result)
        print(fact.related_letter)
    return(addletter)

def Check_rule(Rules_list,fact, letter,it):
    addletter = 0
    tmp = []
    for rule in Rules_list:
        if letter in rule.expression:
            addletter += rule_dissec(rule,fact)
            if rule not in fact.tree:
                tmp.append(rule)
        elif letter in rule.result:
            addletter += rule_dissec(rule,fact)
            if rule not in fact.tree:
                tmp.append(rule)
    for l in fact.related_letter:
        if addletter == 0:
            break
        fact.tree.append(tmp)
        Check_rule(Rules_list,fact,l,it+1)

#for letter in Query_list.query_list: // TEST AVEC LA LETTRE G:
fact = Query_list.query_list[0]
print("QUERY_LETTER:", fact.letter)
Check_rule(Rules_list,fact, fact.letter, 0)
print("LETTER_LIST: ", fact.related_letter)
for t in fact.tree:
    for y in t:
        print(" TREE: ",y.expression,y.implication, y.result, end="")
    print()
