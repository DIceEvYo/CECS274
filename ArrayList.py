import numpy as np
from Interfaces import List

class ArrayList(List):

    '''
        ArrayList: Implementation of a List interface using Arrays. 
    '''


                                            # Init | Default Array List Settings
    ''' 
    Time Complexity: O(n)
    '''

    def __init__(self):
        '''
        __init__: Initialize the state (array, n and j). 
        '''

        self.a = self.new_array(1)
        #a = new_array size of 1
        self.n = 0
        #number of elements
        self.j = 0
        #could be considered position of head

        #i is our input index variable


                                                        # New Array
    ''' 
    Time Complexity: O(n)
    '''

    def new_array(self, n : int) ->np.array:
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

        if(gs):
            #If value is True, the array size will grow (2x)

            temp = self.new_array(max(1,(int)(2*len(self.a))))
        else:
            #If value is False, the array size will shrink (1/2x)

            temp = self.new_array(max(1, (int) (len(self.a)/2)))
            # Create temporary array, of size len(a)/2
        for temp_index in range(0,self.n):
            temp[temp_index] = self.a[(self.j+temp_index)%len(self.a)]
        #append array a's values to temp array
        self.a = temp
        #replace a with new array
        self.j = 0
        #reset j's value


                                                    # Get | Retrieving an Index
    ''' 
    Time Complexity: O(1)
    '''

    def get(self, i : int) -> object:
        '''
        get: returns the element at position i
        Inputs:
            i: Index that is integer non negative and at most n
        '''

        if(self.index_expectations(i)): return self.a[(i+self.j)%len(self.a)]
        #If provided index input is valid, value of the provided index is returned
        else:
            raise IndexError
            #raise Exception("Provided index is out of bounds. Please provide a different index.")
        #Exception is raised if index requirements aren't met.


                                                    # Index Expectations
    ''' 
    Time Complexity: O(1)
    '''

    def index_expectations(self, i : int) -> bool:
        '''
        for given index inputs we need to be sure that the index
        is valid, that it's within the array's domain of 0 to len(a)
                             0 <= i < len(a)
        '''

        if(0 <= i < len(self.a)):
            return True
        #Expectations are met, given index i is within the array's domain.
        else:
            False
        #Expectations have not been met, given index i is out of bounds.


                                                    # Set | Setting Values
    ''' 
    Time Complexity: O(1)
    '''

    def set(self, i : int, val : object) -> object:
        '''
        set: Set the value new_val at the index i.
        Inputs:
            i: Index that is integer non negative and at most n
            new_val: Object type, i.e., any object
        '''

        if (self.index_expectations(i)):
            prev_val = self.a[(i+self.j)%len(self.a)]
            self.a[(i + self.j) % len(self.a)] = val
            return prev_val
            # If provided index input is valid, the previous/replaced value of the index is returned
        else:
            raise IndexError
            #raise Exception("Provided index is out of bounds. Please provide a different index.")
            #Exception is raised if index requirements aren't met.


                                            # Append | Adding Values @ index n
    ''' 
    Time Complexity: O(n)
    '''

    def append(self, val : object) :
        self.add(self.n, val)
        #Value's added to the end of the list, n


                                    # Side | First Half or Second Half? Left or Right?
    ''' 
    Time Complexity: O(1)
    '''

    def side(self, i) -> bool:
        if(i < ((self.n)/2)): return True
        #If True is returned, we're working w/ the first half a.k.a the left side of the array
        else: return False
        #If False is returned, we're working w/ the second half a.k.a the right side of the array


                                                # Add | Adding Values
    ''' 
    Time Complexity: O(n)
    '''

    def add(self, i : int, val : object) :
        '''
            add: shift one position all the items j>=i, insert an element 
            at position i of the list and increment the number of elements 
            in the list
            Inputs:
                i: Index that is integer non negative and at most n
                val: Object type, i.e., any object
        '''

        if(self.n == len(self.a)): self.resize(True)
        #If len(a) = n upon adding, the array must be resized (growth)

        if(self.index_expectations(i)):
            if(self.side(i)):
                #First Half | Left i<n/2

                self.j = (self.j - 1)%len(self.a)
                #Updating value j
                for temp_index in range(0, i, 1):
                    self.a[(self.j+temp_index)%len(self.a)] = self.a[(self.j+temp_index+1)%len(self.a)]
                    #shifting elements to the left
            else:
                #Second Half | Right i>=n/2

                for temp_index in range (self.n,i, -1):
                    self.a[(self.j+temp_index)%len(self.a)] = self.a[(self.j+temp_index-1)%len(self.a)]
                    #shifting elements to the right
            self.a[(self.j + i) % len(self.a)] = val
            #Adding value val to index i
            self.n+=1
            #Updating Value n
        else:
            raise IndexError
            #raise Exception("Provided index is out of bounds. Please provide a different index.")
        #Exception is raised if index requirements aren't met.


                                                # Remove | Removing Values
    ''' 
    Time Complexity: O(n)
    '''

    def remove(self, i : int) -> object:

        if (self.index_expectations(i) and (self.n > 0)):
            if (self.side(i)):
                #First Half | Left i<n/2

                #Value Removal Test
                x= self.a[(self.j+i)%len(self.a)]
                #Index to Remove
                #print("Removing: ", x)

                for temp_index in range(0, i, 1):
                    self.a[(self.j+temp_index+1)%len(self.a)] = self.a[(self.j+temp_index)%len(self.a)]
                    #shifting elements to the right
                self.j = (self.j+1)%(len(self.a))
                #Updating Value j

            else:
                #Second Half | Right i>=n/2

                #Value Removal Test
                x = self.a[(i+self.j) % len(self.a)]
                #Index to Remove
                #print("Removing: ", x)

                for temp_index in range (self.n-1,i, -1):
                    self.a[(self.j+temp_index-1)%len(self.a)] = self.a[(self.j+temp_index)%len(self.a)]
                    #shifting elements to the left

            self.n -= 1 #Update number of elements
            if (3 * (self.n) < len(self.a)): self.resize(False)
            #If len(a) > 3n after removal, the array must be resized (shrunk)
        else:
            raise IndexError
            #raise Exception("Provided index is out of bounds. Please provide a different index.")
        #Exception is raised if index requirements aren't met.
        return x


                                                # Size | Number of Elements n
    ''' 
    Time Complexity: O(1)
    '''

    def size(self) -> int:
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

    def __str__(self):
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayList
            Return: String with the content of the list
        '''

        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        s += f"] {self.n} : {self.j}"
        return s


                                            # Get Item | Retrieve & Format
    ''' 
    Time Complexity: O(n)
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
            return [self.get(i) for i in range(i.start, i.stop)]
        else:
            return self.get(i)


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
            val = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator +=1
        else:
             raise StopIteration()
        return val


                                                        # Test List
    ''' 
    Time Complexity: O(n)
    '''
'''
s = ArrayList()
try:
    s.remove(0)
except IndexError:
    print("Passed index test")
else:
    print("List remove is not correct")

s.add(0, "a")
print(s)
s.add(1, "c")
print(s)
s.add(1, "b")
print(s)
print("b:", s.remove(1))
s.add(1, "d")
print(s)
print("d:", s.remove(1))
s.add(0, "e")
print(s)
s.add(3, "f")
print(s)
print("c:", s.remove(2))
print(s)
print("f:", s.remove(2))
print(s)
print("a:", s.remove(1))
print(s)
print("e:", s.remove(0))
print(s)
'''

'''
arraylist = ArrayList()
#arraylist.remove(0)
#Checking Append()
print("Appending Values; Adding values to i = n")
arraylist.append("a")
print(arraylist)
arraylist.append("b")
print(arraylist)
arraylist.append("c")
print(arraylist)
arraylist.append("d")
print(arraylist)
arraylist.append("e")
print(arraylist)
arraylist.append("f")
print(arraylist)
arraylist.append("g")
print(arraylist)
arraylist.append("h")
print(arraylist)
#Checking First Half Removal
print("Testing First Half Removal; Removing values @ i = n-1")
arraylist.remove(arraylist.n-1)
print(arraylist)
arraylist.remove(arraylist.n-1)
print(arraylist)
arraylist.remove(arraylist.n-1)
print(arraylist)
arraylist.remove(arraylist.n-1)
print(arraylist)
arraylist.remove(arraylist.n-1)
print(arraylist)
arraylist.remove(arraylist.n-1)
print(arraylist)
arraylist.remove(arraylist.n-1)
print(arraylist)
arraylist.remove(arraylist.n-1)
print(arraylist)
#Checking Add()
print("Appending Values; Adding values to i = 0")
arraylist.add(0, "a")
print(arraylist)
arraylist.add(0, "b")
print(arraylist)
arraylist.add(0, "c")
print(arraylist)
arraylist.add(0, "d")
print(arraylist)
arraylist.add(0, "e")
print(arraylist)
arraylist.add(0, "f")
print(arraylist)
arraylist.add(0, "g")
print(arraylist)
arraylist.add(0, "h")
print(arraylist)
#Checking Second Half Removal
print("Testing Second Half Removal; Removing values @ i = 0")
arraylist.remove(0)
print(arraylist)
arraylist.remove(0)
print(arraylist)
arraylist.remove(0)
print(arraylist)
arraylist.remove(0)
print(arraylist)
arraylist.remove(0)
print(arraylist)
arraylist.remove(0)
print(arraylist)
arraylist.remove(0)
print(arraylist)
arraylist.remove(0)
print(arraylist)
'''

