"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()
            
    def add_edge(self, i : int, j : int):
        self.adj[i].append(j)

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, object)

    def remove_edge(self, i : int, j : int):
        l = self.adj[i]
        for k in (0, l.size()-1):
            if l.get(k) == j:
                l.remove(k)
                return
                
    def has_edge(self, i : int, j: int) ->bool:
        l = self.adj[i]
        for k in (0, l.size()):
            if l.get(k) == j:
                return True
        return False
        
    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, j) -> List:
        out = ArrayList()
        for i in range (0, self.n):
            if self.has_edge(i,j):
                out.append(i)
        return out

    def bfs(self, r :int):
        seen = self.new_array(self.n)
        #p = self.new_array(self.n)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        #p[r] = r
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            #ngh = g.out_edges(i)
            for j in (self.out_edges(i)):
                #j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    seen[j] = True
                    #p[j] = i

    def shortestPath(self, Graph, r):
        seen = self.new_array(self.n)
        p = self.new_array(self.n)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        p[r] = r
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            ngh = g.out_edges(i)
            for k in range(0, ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    seen[j] = True
                    p[j] = i
        return p

    def distance(self, r, dest):
        p = self.shortestPath(r)
        d = 0
        while dest != p[dest]:
            dest = p[dest]
            d += 1
        return d

    def dfs(self, r):
        seen = self.new_array(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        while s.size() > 0:
            i = s.pop()
            if seen[i] == False:
                seen[i] == True
                ngh = self.out_edges(i)
                for k in range(0, ngh.size()):
                    j = ngh.get(k)
                    s.push(j)
    '''
    def dfs(self, g, r :int):
        c = self.new_array(g.n)
        self.dfs2(g,r,c)
        
    def dfs2(self, g, i , c):
        c[i] = "grey"
        for j in g.out_edges(i):
            if c[j] == "white":
                c[j] = "grey"
                self.dfs2(g,j,c)
        c[i] = "black"
    '''
    
    def distance(self, r : int, dest: int):
        pass

    def size(self) -> int :
        return self.n
                      
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

'''
g = AdjacencyList(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)
#g.remove_edge(1,2)
print(g)
print(g.bfs(1))
'''



