import random 
from Interfaces import Queue 
import ArrayQueue


class RandomQueue(Queue):

    '''
        RandomQueue: Implementation of a ArrayQueue interface using Arrays and Randomness.   (L O L)
    '''

########################################################################################################################
                                            # Init | Default Array Queue Settings
    ''' 
        Time Complexity: O(n)
    '''

    def __init__(self):
        self.queue = ArrayQueue.ArrayQueue()

########################################################################################################################
                                                        # Add
    ''' 
        Time Complexity: O(n)
    '''

    def add(self, x : object):
        '''
            add: Add the value x to the Queue
            Inputs:
                x: Object type, i.e., any object
        '''
        self.queue.add(x)

########################################################################################################################
                                                        # Remove Rand
    ''' 
        Time Complexity: O(n)
    '''

    def remove(self) -> object:
        '''
            remove: remove the next (previously added) value, y, from the
                    Queue and return y. The Queue’s queueing discipline 
                    decides which element should be removed.
                                            Just joking, just remove something random lol.
            Return: Object type
        '''
        if ((0 >= self.queue.n)):
            # raise IndexError
            raise Exception("Provided index is out of bounds. Please provide a different index.")
        random_index = random.randint(0, self.queue.size()-1) #Random Integer that's in range of the array's size.
        #print("RI: ", random_index)
        val = self.queue.a[random_index]  # Value to be removed
        for temp_index in range(random_index, self.queue.n - 1):
            self.queue.a[temp_index] = self.queue.a[temp_index + 1]
        self.queue.n -= 1
        if (3 * (self.queue.n) < len(self.queue.a)): self.queue.resize(False)  # If len(a) > 3n after removal, the array must be resized (shrunk)
        return val  # Value that's removed, will be returned

########################################################################################################################
                                                            # Size
    ''' 
        Time Complexity: O(1)
    '''

    def size(self) -> int:
        return self.queue.size()

########################################################################################################################
                                                    # Test Queue
    ''' 
        Time Complexity: O(n)
    '''
'''
# Checking Add()
randomQueue = RandomQueue()
print("Adding Values; Adding values to i = (self.j+self.n)%len(self.a)")
randomQueue.add("a")
print(randomQueue.queue)
randomQueue.add("b")
print(randomQueue.queue)
randomQueue.add("c")
print(randomQueue.queue)
randomQueue.add("d")
print(randomQueue.queue)
randomQueue.add("e")
print(randomQueue.queue)
randomQueue.add("f")
print(randomQueue.queue)
randomQueue.add("g")
print(randomQueue.queue)
randomQueue.add("h")
print(randomQueue.queue)
# Checking Random Dance Removes
print("Testing Removal; Removing random values")
randomQueue.removeRand()
print(randomQueue.queue)
randomQueue.removeRand()
print(randomQueue.queue)
randomQueue.removeRand()
print(randomQueue.queue)
randomQueue.removeRand()
print(randomQueue.queue)
randomQueue.removeRand()
print(randomQueue.queue)
randomQueue.removeRand()
print(randomQueue.queue)
randomQueue.removeRand()
print(randomQueue.queue)
randomQueue.removeRand()
print(randomQueue.queue)
'''
