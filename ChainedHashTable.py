from Interfaces import Set
from DLList import DLList
import numpy as np

class ChainedHashTable(Set):
    class Node() :
        def __init__(self, key, value) :

            #Every node holds a key and a value
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList) :

        #This chained hashtable will consist of dll per index of the array
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2**self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):

        #Zeros are allocated to empty spots of the array
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.dtype()
        return t


    def hash(self, key : int) -> int :

        #Hash(key) = (Z*hash(key)%(2^w))/(2^(w-d))
        #Value is allocated to a certain position of the CHT based on the key
        return self.z * hash(key) % (2**self.w) >> (self.w - self.d)

    def size(self) -> int:

        #Return number of elements, n.
        return self.n

    def find(self, key : object) -> object :

        #key needs to exist
        if (key == None): raise IndexError
        #attempting to find key, if found, will be returned
        for i in range (0, self.t[self.hash(key)].size()):
            if(self.t[self.hash(key)].get(i).key == key):
                return self.t[self.hash(key)].get(i).value
        return None


    def add(self, key : object, value : object) :

        if (self.find(key) != None): return False
        if self.n+1 > len(self.t): self.resize()
        self.t[self.hash(key)].add(0, self.Node(key,value))
        self.n += 1
        return True


    def remove(self, key : int)  -> object:

        if(key == None): raise IndexError
        for i in range(0,self.t[self.hash(key)].size()):
            if(self.t[self.hash(key)].get(i).key == key):
                self.t[self.hash(key)].remove(i)
                self.n -= 1
                if len(self.t) >= (3*self.n): self.resize()
                return True
        return False


    def resize(self):

        if (self.n == len(self.t)):
            self.d += 1
        else:
            self.d -= 1
        a = self.alloc_table(2**self.d)
        for j in range(0, len(self.t)):
            for i in range (0, self.t[j].size()):
                a[self.hash(self.t[j].get(i).key)].add(0, (self.t[j].get(i)))
                #l = self.t[j]
                #u = l.get(i)
                #a[self.hash(u.key)].add(0,u)
        self.t = a


    def __str__(self):

        #Table is printed at a string
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"

