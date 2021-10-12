from Interfaces import Stack
import SLLStack

class MaxStack(Stack) :
    def __init__(self):
        #O(1)
        self.stack = SLLStack.SLLStack()
        self.maximum = None
        
    def max(self) ->object:
        '''
            Returns the max element
            O(1)
        '''
        return self.maximum
    
    def push(self, x : object) : 
        '''
            push: Insert an element in the tail of the stack 
            Inputs:
                x: Object type, i.e., any object
            O(1)
        '''
        if(self.maximum == None) or (x > self.maximum):
            self.maximum = x
        self.stack.push(x)


    def pop(self) -> object:
        '''
            pop: Remove the last element in the stack 
            Returns: the object of the tail if it is no empty
            O(1) for Pop
            O(n) for finding new Max val
        '''
        t = self.stack.pop()
        try:
            if(self.maximum == t):
                if(self.stack.size() != 0):
                    self.maximum = 0
                    u = self.stack.head
                    for i in range (0, self.stack.size()):
                        if((self.maximum == None) or (u.x > self.maximum)):
                            self.maximum = u.x
                        u = u.next
        except: return t
        return t


    def size(self) -> int:
        #Returns size of stack, time should be O(1)
        return self.stack.size()

