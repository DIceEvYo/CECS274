from BinarySearchTree import BinarySearchTree
from Interfaces import Set
from DLList import DLList


class BinarySearchTreeWithDuplication(Set):

    def __init__(self, nil=None):
        self.BinarySearchTree = BinarySearchTree()
        self.n = 0
        
    def size(self) -> int:
        return self.n 

    def find(self, x: object) -> object:
        t = ''
        for i in self.BinarySearchTree.find(x):
            t += i
            t += ","
        t = t[:len(t) - 1]
        return t


    def add(self, key : object, value : object) -> bool:
        if self.BinarySearchTree.find(key) == None:
            d = DLList()
        else:
            d = self.BinarySearchTree.find(key)
        d.append(value)
        self.BinarySearchTree.add(key, d)

    
    def remove(self, x : object) -> bool:
        if (self.BinarySearchTree.find(x) != None):
            d = self.BinarySearchTree.find(x)
            return d.remove(0)

    def in_order(self):
        self.BinarySearchTree.in_order()

'''
q = BinarySearchTreeWithDuplication()
q.add(1, "a")
q.add(1, "b")
q.add(2, "c")
q.add(3, "d")
q.add(3, "e")
q.in_order()
print(q.find(1))
print(q.find(2))
print(q.find(3))
'''