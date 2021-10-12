from Interfaces import Queue
import numpy as np

class SLLQueue(Queue):
#FIFO

    class Node:
                                                    # NODE | Initialization
        '''
        Time Complexity: O(1)
        '''

        def __init__(self, x: np.object):
            self.next = None  # Newly Created Node points to None.
            self.x = x  # Node's Value is set to provided Value.

                                                # Linked List | Initialization
    '''
    Time Complexity: O(1)
    '''

    def __init__(self):
        self.head = None
        # Head of the newly created Linked List points to None.
        self.tail = None
        # Tail of the newly created Linked List points to None.
        self.n = 0

        # Number of elements in a newly created list, should be 0.
        
                                            # Add | Add New Node to the Tail/End of the List
    '''
    Time Complexity: O(1)
    '''

    def add(self, x :np.object) :
        u = self.Node(x)
        #New Node is created
        if (self.n == 0):
        #If there's no elements
            self.head = u
            #The Head will be set to the new node
        else:
            self.tail.next = u
            #Tail points to new node
        self.tail = u
        #Tail is set to new node
        self.n += 1
        #Number of elements, value n, is updated
        return True

                                        # Pop | Remove Node from the Head of the List
    '''
    Time Complexity: O(1)
    '''

    def remove(self) -> np.object:

        #This code is exactly the same as pop() in SLLStack(). Both of these methods will remove the Head of the List.

        if (self.n == 0): raise IndexError
        # Can't remove an element that doesn't exist.
        x = self.head.x
        # Temp variable x is set to value to be removed.
        self.head = self.head.next
        # The Head is equal to its next element (pretty much the removal statement) [Head, Next,...] -> [Next,...]
        self.n -= 1
        # Number of elements is updated
        if self.n == 0:
            # If there are no more elements
            self.tail = None
            # Tail should also equal None
        return x
        # Value that was removed should be returned.

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
