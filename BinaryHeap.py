import numpy as np
from Interfaces import Queue



def left(i : int):
    if i< 0: raise IndexError()
    return 2*i + 1

def right(i: int):
    if i< 0: raise IndexError()
    return 2*(i+1)

def parent(i : int):
    if i< 0: raise IndexError()
    return (i-1)//2

class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0
        self.j = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, object)

    def resize(self, gs):
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


    def add(self, x : object):
        if len(self.a) == self.n:
            self.resize(True)
        self.a[self.n] = x
        self.n += 1
        self.bubble_up(self.n-1)


    def bubble_up(self, i):
        if i < 0 or i > self.n: raise IndexError
        p = parent(i)
        while i > 0 and self.a[i] < self.a[p]:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p
            p = parent(i)


    def remove(self):
        if self.n == 0: raise IndexError
        x = self.a[0]
        self.a[0],self.a[self.n-1] = self.a[self.n-1], self.a[0]
        self.n = self.n-1
        self.trickle_down(0)
        if 3*self.n < len(self.a):
            self.resize(False)
        return x


    def trickle_down(self, i):
        while i >= 0:
            j = -1
            r = right(i)
            if r < self.n and self.a[r] < self.a[i]:
                l = left(i)
                if self.a[l] < self.a[r]:
                    j = l
                else:
                    j = r
            else:
                l = left(i)
                if l < self.n and self.a[l] < self.a[i]:
                    j = l
            if j>=0:
                    self.a[j],self.a[i] = self.a[i],self.a[j]
            i = j

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"

