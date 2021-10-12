import numpy as np
from Interfaces import Queue

class ArrayQueue(Queue):

    '''
        ArrayQueue: Implementation of a Queue interface using Arrays.   (First  In   First  Out)
    '''


                                            # Init | Default Array Queue Settings
    ''' 
    Time Complexity: O(n)
    '''

    def __init__(self):
        '''
        __init__: Initialize the state (array, n and j).
        '''

        self.a = self.new_array(1)
        # a = new_array size of 1
        self.n = 0
        # number of elements
        self.j = 0
        # could be considered position of head

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
        #O(n) function since np.zeros works with arrays


                                            # Resize | Array Space Management
    ''' 
    Time Complexity: O(n)
    '''

    def resize(self, gs: bool):
        '''
        #resize: Create a new array and copy the old values. Value j will be set to zero. (J returns to the head of the array)
        '''

        if (gs):
            # If value is True, the array size will grow (2x)

            temp = self.new_array(max(1, (int)(2 * len(self.a))))
        else:
            # If value is False, the array size will shrink (1/2x)

            temp = self.new_array(max(1, (int)(len(self.a) / 2)))
            # Create temporary array, of size len(a)/2
        for temp_index in range(0, self.n):
            temp[temp_index] = self.a[(self.j + temp_index) % len(self.a)]
        # append array a's values to temp array
        self.a = temp
        # replace a with new array
        self.j = 0
        # reset j's value


                                                    # Add | Adding Values
    ''' 
    Time Complexity: O(1)
    '''

    def add(self, val : object) :
        '''
            shift all j > i one position to the right
            and add element val in position i
        '''

        if (self.n == len(self.a)): self.resize(True)
        # If len(a) = n upon adding, the array must be resized (growth)
        self.a[(self.j+self.n)%len(self.a)] = val
        self.n += 1
        return True



    def remove(self) -> object :
        '''
            remove the first element in the queue
        '''

        if ((0>=self.n)):
            raise IndexError
            #raise Exception("Provided index is out of bounds. Please provide a different index.")
        else:
            val = self.a[self.j]
            # Value to be removed
            self.j = (self.j+1)%len(self.a)
            # Value j is updated
            self.n = self.n-1
            # Value n is updated
            if (3 * (self.n) < len(self.a)): self.resize(False)
            # If len(a) > 3n after removal, the array must be resized (shrunk)
            return val
            # Removed value is returned
    

                                                # Size | Number of Elements n
    ''' 
    Time Complexity: O(1)
    '''

    def size(self) :
        '''
            size: Returns the size of the queue
            Return: an integer greater or equal to zero representing the number
                    of elements in the queue
        '''
        return self.n


                                                # Str | Returns Array as a String
    ''' 
    Time Complexity: O(n)
    '''

    def __str__(self):
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayQueue
            Return: String with the content of the queue
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
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


                                                    # Test Queue
    ''' 
        Time Complexity: O(n)
    '''
'''
# Checking Add()
arrayQueue = ArrayQueue()
print("Adding Values; Adding values to i = (self.j+self.n)%len(self.a)")
arrayQueue.add("a")
print(arrayQueue)
arrayQueue.add("b")
print(arrayQueue)
arrayQueue.add("c")
print(arrayQueue)
arrayQueue.add("d")
print(arrayQueue)
arrayQueue.add("e")
print(arrayQueue)
arrayQueue.add("f")
print(arrayQueue)
arrayQueue.add("g")
print(arrayQueue)
arrayQueue.add("h")
print(arrayQueue)
# Checking Second Half Removal
print("Testing Removal; Removing values @ i = j")
arrayQueue.remove()
print(arrayQueue)
arrayQueue.remove()
print(arrayQueue)
arrayQueue.remove()
print(arrayQueue)
arrayQueue.remove()
print(arrayQueue)
arrayQueue.remove()
print(arrayQueue)
arrayQueue.remove()
print(arrayQueue)
arrayQueue.remove()
print(arrayQueue)
arrayQueue.remove()
print(arrayQueue)
'''