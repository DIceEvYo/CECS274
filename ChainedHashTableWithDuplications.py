from Interfaces import Set
from DLList import DLList
import ChainedHashTable 

class ChainedHashTableWithDuplications(Set):
    def __init__(self) :
        self.chainHashTable = ChainedHashTable.ChainedHashTable()
        self.n = 0

    def size(self) -> int:
        return self.n
        
    def find(self, key : object) -> object :
        t = ''
        for i in self.chainHashTable.find(key):
            t += i
            t += ","
        t = t[:len(t)-1]
        return t
        
    def add(self, key : object, value : object) :
        if self.chainHashTable.find(key) == None:
            d = DLList()
        else:
            d = self.chainHashTable.find(key)
        d.append(value)
        self.chainHashTable.add(key, d)


    def remove(self, key : int)  -> object:
        if(self.chainHashTable.find(key) != None):
            d = self.chainHashTable.find(key)
            return d.remove(0)
    
    
    def __str__(self):
        return self.cht.__str__()

