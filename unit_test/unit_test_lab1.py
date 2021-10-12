import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import ArrayStack
import ArrayQueue
import ArrayList
import RandomQueue
import Calculator
import BookStore


class ArrayBasedTest(unittest.TestCase) :
    def test_Queue(self) :
        points = 0.5
        q = ArrayQueue.ArrayQueue()
        try:
            q.remove()
        except IndexError:
            points += 0.5
        else:
            print("Queue remove is not correct")
        try:
            q.add(1)
            q.add(2)
            self.assertAlmostEqual(q.remove(), 1)
            self.assertAlmostEqual(q.remove(), 2)
            q.add(3)
            q.add(4)
            q.add(5)
            self.assertAlmostEqual(q.remove(), 3)
            self.assertAlmostEqual(q.remove(), 4)
            self.assertAlmostEqual(q.remove(), 5)
            points += 1
        except:
            print("Queue is not correct")
        finally:
            print(f"Queue: {points} Points")

    def test_Stack(self) :
        points = 0.5
        s = ArrayStack.ArrayStack()
        try:
            s.pop()
        except IndexError:
            points += 0.5
        else:
            print("Stack pop is not correct")
        try:
            s.push(1)
            s.push(2)
            self.assertAlmostEqual(s.pop(), 2)
            s.push(3)
            self.assertAlmostEqual(s.pop(), 3)
            s.push(4)
            s.push(5)
            self.assertAlmostEqual(s.pop(), 5)
            self.assertAlmostEqual(s.pop(), 4)
            self.assertAlmostEqual(s.pop(), 1)
            points += 1
        except:
            print("Stack is not correct")
        finally:
            print(f"Stack {points} Points")
            

    def test_List(self) :
        points = 0.5
        s = ArrayList.ArrayList()
        try:
            s.remove(0)
        except IndexError:
            points += 0.5
        else:
            print("List remove is not correct")
        try:
            s.add(0, "a")
            s.add(1, "c")
            s.add(1, "b")
            self.assertAlmostEqual(s.remove(1), "b")
            s.add(1, "d")
            self.assertAlmostEqual(s.remove(1), "d")
            s.add(0, "e")
            s.add(3, "f")
            self.assertAlmostEqual(s.remove(2), "c")
            self.assertAlmostEqual(s.remove(2), "f")
            self.assertAlmostEqual(s.remove(1), "a")
            self.assertAlmostEqual(s.remove(0), "e")
            points += 1
        except:
            print("List is not correct")
        finally:
            print(f"List {points} Points")
            

    def test_RandomQueue(self) :
        points = 0.5
        q = RandomQueue.RandomQueue()
        try:
            q.remove()
        except IndexError:
            points += 0.5
        else:
            print("Random Queue remove is not correct")
        try:
            q.add(1)
            q.add(2)
            q.remove()
            self.assertAlmostEqual(q.size(), 1)
            q.add(3)
            q.add(4)
            q.add(5)
            self.assertAlmostEqual(q.size(), 4)
            q.remove()
            q.remove()
            q.remove()
            self.assertAlmostEqual(q.size(), 1)
            points += 1
        except:
            print("Random Queue is not correct")
        finally:
            print(f"Random Queue: {points} Points")

    def test_Calculator(self) :
        a = Calculator.Calculator() 
        points = 0.5
        try:
            self.assertAlmostEqual(a.matched_expression("(A+B)"), True)
            self.assertAlmostEqual(a.matched_expression("(A+B)*(B+C)"), True)
            self.assertAlmostEqual(a.matched_expression(""), True)
            points += 0.5
            self.assertAlmostEqual(a.matched_expression("("), False)
            self.assertAlmostEqual(a.matched_expression(")"), False)
            self.assertAlmostEqual(a.matched_expression("()"), True)
            self.assertAlmostEqual(a.matched_expression("((A+B)/(A*C))*(D+A)"), True)
            points += 1
        except:
            print("Calculator is not correct")
        finally:
            print(f"Calculator: {points} Points")

    def test_BookStore(self) :
        points = 0.5
        try:
            a = BookStore.BookStore()
            self.assertAlmostEqual(a.loadCatalog("../books.txt"), 542684)
            points += 0.5
            self.assertAlmostEqual(a.searchBookByInfix(""), 50)
            self.assertAlmostEqual(a.searchBookByInfix("Tears of the Wor"), 1)
            self.assertAlmostEqual(a.searchBookByInfix("World of Pa"), 4)
            self.assertAlmostEqual(a.searchBookByInfix("World of Ha"), 14)
            points += 1
        except:
            print("BookStore is not correct")
        finally:
            print(f"BookStore: {points} Points")
