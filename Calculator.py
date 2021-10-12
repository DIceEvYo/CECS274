import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import BinaryTree
import operator

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)

    def print_expression(self, s : str) -> str :
        if(self.matched_expression(s)):
            t = ''
            for i in s:
                if(self.dict.find(i) != None):
                    t += (str)(self.dict.find(i))
                else:
                    t += i
            return t

    def matched_expression(self, s : str) -> bool :
        #Checks if parenthesis in the given expression are valid.
        s = self.no_paren(s)
        a = ArrayStack.ArrayStack()
        for i in range(0, len(s)):
            if(s[i] == "("): a.push(s[i])
            elif(s[i] == ")"):
                try: a.pop()
                except: return(False)
        if(len(a) == 0):return(True)
        else: return(False)

    def no_paren(self, exp):
        if not("(" in exp) and not(")" in exp):
            exp = "(" + exp
            exp = exp + ")"
        return exp

    def build_parse_tree(self, exp : str) ->str:
        exp = self.no_paren(exp)
        if(self.matched_expression(exp)):
            t = BinaryTree.BinaryTree()
            t.r = t.Node('')
            u = t.r
            for i in range(0, len(exp)):
                if (exp[i] == "("):
                    u.left = u.insert_left()
                    u = u.left
                elif (exp[i] == ")"):
                    u = u.parent
                elif (exp[i] in ["+", "-", "*", "/"]):
                    u.set_val(exp[i])
                    u.right = u.insert_right()
                    u = u.right
                else:
                        u.set_val(exp[i])
                        u.v = self.dict.find(exp[i])
                        u = u.parent
            t.in_order()
            return t

    def _evaluate(self, u):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if (u.left != None) and (u.right != None):
            return round(op[u.x](self._evaluate(u.left), self._evaluate(u.right)), 2)
        else:
            w = self.dict.find(u.x)
            if w != None: return w
            return u.v

    def evaluate(self, exp):
        try:
            parseTree = self.build_parse_tree(exp)
            return self._evaluate(parseTree.r)
        except:
            try:
                a = ArrayStack.ArrayStack()
            except:
                return 0
        return 0
        


s = Calculator()
print(s.evaluate("((a*b)+(c*d))"))
s.set_variable("a", 1.3)
s.set_variable("b", 2.1)
s.set_variable("c", 2.2)
s.set_variable("d", 3.0)
print(s.evaluate("((a*b)+(c*d))"))
