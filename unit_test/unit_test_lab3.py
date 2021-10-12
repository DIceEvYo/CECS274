import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import ChainedHashTable
import Calculator
import BookStore
import MultipleKeysHashTable


class  ChainedHashTableTest(unittest.TestCase) :
    def test_hashtable(self) :
        points = 0.5
        q = ChainedHashTable.ChainedHashTable()
        try:
            self.assertIsNone(q.find(2))
        except:
            print("ChainedHashTable find is not correct")
        finally:
            points += 0.5
            
        try:
            q.add(1, "first")
            q.add(2, "second")
            q.add(3, "fourth")
            self.assertAlmostEqual(q.size(), 3)
            self.assertAlmostEqual(q.find(3), "fourth")
            q.remove(3)
            self.assertIsNone(q.find(3))
            self.assertAlmostEqual(q.size(), 2)
            q.add(3, "third")
            q.add(4, "fourth")
            q.add(5, "Fifth")
            q.add(6, "sixth")
            self.assertAlmostEqual(q.size(), 6)
            self.assertAlmostEqual(q.find(3), "third")
            points += 1
        except:
            print("ChainedHashTable is not correct")
        finally:
            print(f"ChainedHashTable: {points} Points")
    
    def test_calculator(self) :
        points = 0.5
        s = Calculator.Calculator()
        try:
           self.assertAlmostEqual(s.print_expression(""), "")
        except:
            print("Calculator  is not correct")
        finally:
            points += 0.5
        
        
        try:
            s.set_variable("a", 1.3)
            s.set_variable("b", 2.1)
            self.assertAlmostEqual(s.print_expression("((a*b)+(c*d))"), "((1.3*2.1)+(c*d))")
            s.set_variable("c", 2.2)
            s.set_variable("d", 3.0)
            self.assertAlmostEqual(s.print_expression("((a*b)+(c*d))"), "((1.3*2.1)+(2.2*3.0))")
            points += 1
        except:
            print("Calculator is not correct")
        finally:
            print(f"Calculator {points} Points")
            
    def test_BookStore(self) :
        points = 0.5
        try:
            a = BookStore.BookStore()
            self.assertAlmostEqual(a.loadCatalog("../books.txt"), 542684)
            points += 0.5
            a.addBookByKey("0920541356")
            b = a.removeFromShoppingCart()
            print("Title", b.title)
            self.assertAlmostEqual(b.title, "Stories, Songs & Poetry to Teach Reading & Writing")
            a.addBookByKey("6304844964")
            b = a.removeFromShoppingCart()
            self.assertAlmostEqual(b.title, "The Ice Storm")
           
            points += 1
        except:
            print("BookStore is not correct")
        finally:
            print(f"BookStore: {points} Points")

    def test_MultipleHashTable(self) :
        points = 0
        try:
            a = MultipleKeysHashTable.MultipleKeysHashTable()
            a.add(1, "a")
            a.add(1, "b")
            a.add(1, "c")
            a.add(2, "d")
            a.add(3, "e")
            a.add(3, "z")
            self.assertAlmostEqual(a.find(1).__str__(), "a,b,c")
            self.assertAlmostEqual(a.find(2).__str__(), "d") 
            self.assertAlmostEqual(a.find(3).__str__(), "e,z")
            points += 2
        except:
            pass
        finally:
            print(f"MultipleHashTable: {points} Points")

