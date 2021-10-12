from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
                                                            # NODE | Initialization
        '''
        Time Complexity: O(1)
        '''

        def __init__(self, x : object) :
            self.next = None
            #Node right_points to none
            self.prev = None
            #Node left_points to none
            self.x = x
            #Node's value

                                                        # Linked List | Initialization
    '''
    Time Complexity: O(1)
    '''

    def __init__(self) :
        self.dummy = DLList.Node("")
        #Dummy node is created
        self.dummy.next = self.dummy
        #Dummy points to itself (because there's nothing else to point to)
        self.dummy.prev = self.dummy
        #Dummy points to itself (because there's nothing else to point to)
        self.n = 0
        #There should be no elements when a linked list is created

                                                             # Get Node
    '''
    Time Complexity: O(1+min{i,n-i})
    '''

    def get_node(self, i : int) -> Node:
        if (i < 0 or i> self.n): raise IndexError
        #Raise Index Error if index is out of bounds
        if (i < self.n/2):
        #If index i is part of the first half...
            p = self.dummy.next
            #Set temp variable p to next part of the dummy.
            for k in range (0,i):
                p = p.next
            #Traverse the LinkedList forwards until index i is reached
        else:
        #If index i is part of the second half...
            p = self.dummy
            #Set temp variable p to the dummy node itself.
            for k in range(0, self.n-i):
                p = p.prev
            #Traverse the LinkedList backwards until index i is reached
        return p
        #Return the found Node P

                                                        # Get Node (Value)
    '''
    Time Complexity: O(1+min{i,n-i})
    '''

    def get(self, i) -> object:
        return self.get_node(i).x
        #Return value of node of given index (if the index exists)

                                                      # Set Node (Value)
    '''
    Time Complexity: O(1+min{i,n-i})
    '''

    def set(self, i : int, x : object) -> object:
        u = self.get_node(i)
        #Node U is the node located at index i, waiting to set its value
        y = u.x
        #Temp variable for value to be removed
        u.x = x
        #Replace/Set value
        return y
        #Returns removed value

                                                    # Add Node (Before)
    '''
    Time Complexity: O(1)
    '''

    def add_before(self, w : Node, x : object) -> Node:
        if(w == None): raise IndexError
        u = DLList.Node(x)
        #Creates New Node w/ value x
        u.prev = w.prev
        #Head of u points to tail of w
        u.next = w
        #Tail of u points to w
        u.next.prev = u
        #U.next's head points to u
        u.prev.next = u
        #U.prev's tail points to u
        self.n += 1
        #Number of elements, value n, is updated.
        return u
        #New node, u, is returned.

                                                    # Add Node (Specified)
    '''
    Time Complexity: O(1+min{i,n-i})
    '''

    def add(self, i : int, x : object)  :
        if (i < 0 or i> self.n): raise IndexError
        return self.add_before(self.get_node(i),x)

                                                    # Remove Node (Specified by Node)
    '''
    Time Complexity: O(1)
    '''

    def _remove(self, w: Node):
        if (self.n == 0): raise IndexError
        #Can't remove an element that doesn't exist.
        w.prev.next = w.next
        #W.prev points to w.next
        w.next.prev = w.prev
        #W.next points to w.prev
        self.n -= 1
        #Number of elements, n, updates


                                                    # Remove Node (Specified by Index)
    '''
    Time Complexity: O(1+min{i,n-i})
    '''

    def remove(self, i :int) :
        if (self.n == 0): raise IndexError
        #Can't remove an element that doesn't exist.
        w = self.get_node(i)
        #w is node at index i (if it exists)
        t = w.x
        #Value of node to be removed is placed in variable t
        w.prev.next = w.next
        #The node before w points to the node after w
        w.next.prev = w.prev
        #The node after w points to the node before w
        self.n -= 1
        #Number of elements value n is updated
        return t
        #Value of removed node is returned

                                                            # Size
    '''
    Time Complexity: O(1)
    '''

    def size(self) -> int:
        return self.n

                                            # Append | Add Node to End of Linked List
    '''
    Time Complexity: O(1+min{i,n-i})
    '''

    def append(self, x : object)  :
        self.add(self.n, x)

                                            # isPalindrome | Is the Linked List in Palidrome?
    '''
    Time Complexity: O(1+min{n/2})
    '''

    def isPalindrome(self) -> bool :
        if(self.n == 0): return True
        u = self.dummy.next
        #U is at position of head
        w = self.dummy.prev
        #W is at position of tail
        while u != w:
        #While nodes u and w aren't equal to eachother...
            if(u.x != w.x):
                return False
            #If values of nodes u and w are not equal to eachother, False is returned
            u = u.next
            #U shifts right towards center
            w = w.prev
            #W shifts left towards center
        return True
        #True is returned if no inequality of values are found

                                            # Reverse | Reversing the Linked List
    '''
    Time Complexity: O(n)
    '''

    def reverse(self) :
        if self.n != 0:
        #If there's something in the Linked List...
            u = self.dummy
            #Temp node u is set to the head
            v = None
            #Temp node v is set to None
            w = None
            #Temp node w is set to None
            breakfun = 0
            #Temp variable BreakFunction is set to 0
            while u != None and breakfun != None:
            #As long as temp node u is a node, and the breakFunction variable hasn't been set to None...
                w = u.next
                #Temp node w is set to the next element of head
                if(w == None): breakfun = None
                #Don't want temp node w to not be a node
                u.next = v
                #Next element of head is set to None (first time), next time will be set to the element that preceeds it
                v = u
                #Temporary node v, also known as u's preceeding node, will be set to u
                u = w
                #u sets itself to w, also known as u.next
                self.dummy = v
                #Tail is set to the node that preceeds u.

                                                # Str | Returns Linked List as a String
    ''' 
    Time Complexity: O(1)
    '''

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

                                                            # Get Item
        ''' 
        Time Complexity: O(1+min{i,n-i})
        '''
        
    def __getitem__(self, i) -> object:
        '''
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input: 
                i: positive integer less than n
            Return: the item at index i
        '''
        if isinstance(i, slice):
            raise "Not implemented. Please use the references next and prev"
        else:
            return self.get(i)

                                                            # Iterator
    ''' 
    Time Complexity: O(1)
    '''

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

                                                        # Next | Iteration
    ''' 
    Time Complexity: O(1)
    '''

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

'''
test = DLList()
test.add(0,1)
test.add(0,2)
test.add(0,3)
test.add(0,4)
test.add(0,5)
print(test)
test.reverse()
print(test)
'''