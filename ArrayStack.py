import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):

    '''
        ArrayStack: Implementation of the Stack interface based on Arrays. 
        All the @abstractemethods should be implemented.
        An instance of ArrayStack has access to all the methods in ArrayStack and 
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For example,
        s = ArrayStack()
        print(s)
        print(len(s))
    '''


                                            # Init | Default Array Queue Settings
    ''' 
    Time Complexity: O(n)
    '''

    def __init__(self):
        '''
        __init__: Initialize the state (array, n).
        '''

        self.a = self.new_array(1)
        # a = new_array size of 1
        self.n = 0
        # number of elements

        # i is our input index variable


                                                        # New Array
    ''' 
    Time Complexity: O(n)
    '''

    def new_array(self, n: int) ->np.array:
        '''
                new_array: Create a new array of size n
                Input:
                    n: the size of the new array
                Return:
                    An array of size n
                '''

        return np.zeros(n, object)
        # O(n) function since np.zeros works with arrays


                                                # Resize | Array Space Management
    ''' 
    Time Complexity: O(n)
    '''

    def resize(self, gs: bool):
        '''
        #resize: Create a new array and copy the old values.
        '''

        if (gs):
            # If value is True, the array size will grow (2x)

            temp = self.new_array(max(1, (int)(2 * len(self.a))))
        else:
            # If value is False, the array size will shrink (1/2x)

            temp = self.new_array(max(1, (int)(len(self.a) / 2)))
            # Create temporary array, of size len(a)/2
        for temp_index in range(0, self.n):
            temp[temp_index] = self.a[temp_index]
        # append array a's values to temp array
        self.a = temp
        # replace a with new array


                                                    # Get Item | Retrieve
    ''' 
    Time Complexity: O(1)
    '''

    def get(self, i : int) -> object:
        if(self.index_expectations(i)): return self.a[i]
        #Returns value of index i.
        else:
            raise IndexError
            #raise Exception("Provided index is out of bounds. Please provide a different index.")
        # Exception is raised if index requirements aren't met.


                                                    # Set Item | Replace
    ''' 
    Time Complexity: O(1)
    '''

    def set(self, i : int, val : object) -> object:
        if(self.index_expectations(i)):
            x = self.a[i]
            #Value to be replaced
            self.a[i] = val
            #Setting a[i]'s new value
            return x
            #Returning the value that was replaced.
        else:
            raise IndexError
            #raise Exception("Provided index is out of bounds. Please provide a different index.")
        # Exception is raised if index requirements aren't met.


                                                    # Index Expectations
    ''' 
    Time Complexity: O(1)
    '''

    def index_expectations(self, i: int) -> bool:
        '''
        for given index inputs we need to be sure that the index
        is valid, that it's within the array's domain of 0 to len(a)
                                 0 <= i < len(a)
        '''
        if (0 <= i < len(self.a)):
            return True
        # Expectations are met, given index i is within the array's domain.
        else:
            False
        # Expectations have not been met, given index i is out of bounds.


                                                             # Add
    ''' 
    Time Complexity: O(n)
    '''

    def add(self, i: int, val : object) :
        '''
            shift all elements greater than > i one position to the right
            and add element val in position i
        '''
        if (self.n == len(self.a)): self.resize(True)
        # If len(a) = n upon adding, the array must be resized (growth)
        if(self.index_expectations(i)):
            for temp_index in range(self.n, i-1, -1):
                self.a[temp_index] = self.a[temp_index-1]
            self.a[i] = val
            self.n += 1
            #print("n: " , self.n)
        else:
            raise IndexError
            #raise Exception("Provided index is out of bounds. Please provide a different index.")
        # Exception is raised if index requirements aren't met.


                                                             # Remove
    ''' 
    Time Complexity: O(n)
    '''

    def remove(self, i : int) -> object :
        '''
            remove element i and shift all elements greater than i one
            position to the left
        '''
        if (self.index_expectations(i)):
            val = self.a[i]
            #Value to be removed
            for temp_index in range(i, self.n-1):
                self.a[temp_index] = self.a[temp_index+1]
            self.n -= 1
            if (3 * (self.n) < len(self.a)): self.resize(False)
            # If len(a) > 3n after removal, the array must be resized (shrunk)
            return val
            #Value that's removed, will be returned
        else:
            raise IndexError
            #raise Exception("Provided index is out of bounds. Please provide a different index.")
        # Exception is raised if index requirements aren't met.


                                                # Push | Adding the Last Element
    ''' 
    Time Complexity: O(n)
    '''

    def push(self, x : object) :
        self.add(self.n, x)


                                                # Pop | Removing the Recent/Last Element
    ''' 
    Time Complexity: O(n)
    '''

    def pop(self) -> object :
        return self.remove(self.n-1)


                                            # Size | Number of Elements n
    ''' 
    Time Complexity: O(1)
    '''

    def size(self) :
        '''
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        '''
        return self.n


                                            # Str | Returns Array as a String
    ''' 
    Time Complexity: O(n)
    '''

    def __str__(self) -> str:
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"


                                                        # Iterator
    ''' 
    Time Complexity: O(1)
    '''

    def __iter__(self):
        self.iterator = 0
        return self


                                                    # Next | Iteration
    ''' 
    Time Complexity: O(1)
    '''

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x


                                                        # Test List
    ''' 
    Time Complexity: O(n)
    '''
'''
arraystack = ArrayStack()
print("Testing Push")
arraystack.remove(0)
arraystack.push("a")
print(arraystack)
arraystack.push("b")
print(arraystack)
arraystack.push("c")
print(arraystack)
arraystack.push("d")
print(arraystack)
arraystack.push("e")
print(arraystack)
arraystack.push("f")
print(arraystack)
arraystack.push("g")
print(arraystack)
arraystack.push("h")
print(arraystack)
print("Testing Pop")
arraystack.pop()
print(arraystack)
arraystack.pop()
print(arraystack)
arraystack.pop()
print(arraystack)
arraystack.pop()
print(arraystack)
arraystack.pop()
print(arraystack)
arraystack.pop()
print(arraystack)
arraystack.pop()
print(arraystack)
arraystack.pop()
print(arraystack)
print("Testing Add(); Adding values to i = 0")
arraystack.add(0, "a")
print(arraystack)
arraystack.add(0, "b")
print(arraystack)
arraystack.add(0, "c")
print(arraystack)
arraystack.add(0, "d")
print(arraystack)
arraystack.add(0, "e")
print(arraystack)
arraystack.add(0, "f")
print(arraystack)
arraystack.add(0, "g")
print(arraystack)
arraystack.add(0, "h")
print(arraystack)
#Checking Second Half Removal
print("Testing Removal; Removing values @ i = 0")
arraystack.remove(0)
print(arraystack)
arraystack.remove(0)
print(arraystack)
arraystack.remove(0)
print(arraystack)
arraystack.remove(0)
print(arraystack)
arraystack.remove(0)
print(arraystack)
arraystack.remove(0)
print(arraystack)
arraystack.remove(0)
print(arraystack)
arraystack.remove(0)
print(arraystack)
'''