from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
#LIFO

    class Node:
                                                    # NODE | Initialization
        '''
        Time Complexity: O(1)
        '''

        def __init__(self, x : np.object) :
            self.next = None #Newly Created Node points to None.
            self.x = x #Node's Value is set to provided Value.


                                                # Linked List | Initialization
    '''
    Time Complexity: O(1)
    '''

    def __init__(self) :
        self.head = None
        #Head of the newly created Linked List points to None.
        self.tail = None
        #Tail of the newly created Linked List points to None.
        self.n = 0
        #Number of elements in a newly created list, should be 0.

                                            # Push | Add New Node to Head of the List
    '''
    Time Complexity: O(1)
    '''

    def push(self, x : np.object) :
        new_Node = self.Node(x)
        #New Node is created [N]-> Null
        new_Node.next = self.head
        #New Node points to Head [N] -> [Head, U]
        self.head = new_Node
        #New Node becomes head of the list, pointing to the previous head of the list. [Head, N] -> [U]
        if (self.n == 0):
            #If the number of elements is zero, the tail will also equal the head and the new node. [Head, N, Tail]
            self.tail = new_Node
        self.n += 1
        #Number of elements is updated.

                                            # Pop | Remove Node from the Head of the List
    '''
    Time Complexity: O(1)
    '''

    def pop(self) -> np.object:
        if (self.n == 0): raise IndexError
        #Can't remove an element that doesn't exist.
        x = self.head.x
        #Temp variable x is set to value to be removed.
        self.head = self.head.next
        #The Head is equal to its next element (pretty much the removal statement) [Head, Next,...] -> [Next,...]
        self.n -= 1
        #Number of elements is updated
        if self.n == 0:
        #If there are no more elements
            self.tail = None
            #Tail should also equal None
        return x
        #Value that was removed should be returned.

                                                            # Size
    '''
    Time Complexity: O(1)
    '''

    def size(self) -> int:
        return self.n

                                            # Str | Returns Linked List as a String
    ''' 
    Time Complexity: O(1)
    '''

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

                                                            # Iterator
    ''' 
    Time Complexity: O(1)
    '''

    def __iter__(self):
        self.iterator = self.head
        return self

                                                        # Next | Iteration
    ''' 
    Time Complexity: O(1)
    '''

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x




