"""Implementations of some sorting"""
import random
from math import floor


def merge(a0, a1, a):
    i0 = 0
    i1 = 0
    for i in range(0, len(a)):
        if i0 == len(a0):
            a[i] = a1[i1]
            i1 += 1
        elif i1 == len(a1):
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1

def merge_sort(a):
    if len(a) <= 1: return a
    m = floor((len(a))/2)
    a0 = merge_sort(a[0:m])
    a1 = merge_sort(a[m:len(a)])
    merge(a0,a1,a)
    return a


def _quick_sort(a, i, n):
    if n <= 1: return
    while n > len(a):
        n -= 1
    x = a[i + int(random.randrange(0, (n-1)))]
    p = i - 1
    j = i
    q = i + n
    if q >= len(a)+1:
        q -= 1
    while j < q:
        if a[j] < x:
            p += 1
            a[j], a[p] = a[p],a[j]
            j += 1
        elif a[j] > x:
            q -= 1
            a[j], a[q] = a[q], a[j]
        else:
            j += 1
    #print("Test: ", a)
    _quick_sort(a, i, p-i+1)
    _quick_sort(a, q, n-(q-1))


def quick_sort(a):
    _quick_sort(a, 0, len(a))
    return a
    
def binary_search(a, x):
    m = _binary_search(a, len(a), x)
    return m

def _binary_search(a, n, x) :
    l = 0
    r = n - 1
    while r > l:
        m = floor((l + r) / 2)
        if x <= a[m]:
            r = m
        else:
            l = m + 1
    if a[l] == x:
        return l
    else:
        return -1

#a = [3,4,5,2,1]
#a = [1,2,3,4,5]

#print(merge_sort(a), [1,2,3,4,5])
#print(quick_sort(a), [1,2,3,4,5])
#print(binary_search(a, 5))