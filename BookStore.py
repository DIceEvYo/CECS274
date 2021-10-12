import algorithms
import Book
import SortableBook
import ArrayQueue
import ArrayList
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import AdjacencyList
import time
import DLList
import MaxStack



class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = ArrayList.ArrayList()
        self.shoppingCart = MaxStack.MaxStack()
        self.indexKey = ChainedHashTable.ChainedHashTable()
        self.indexSortedPrefix = BinarySearchTree.BinarySearchTree()
        self.bookSortedCatalog = ArrayList.ArrayList()
        self.similarGraph = AdjacencyList.AdjacencyList(0)
        self.bestSeller = BinaryHeap.BinaryHeap()

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        with open(fileName,encoding='utf8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                sb = SortableBook.SortableBook(key, title, group, rank, similar)
                #self.bookCatalog.append(b)
                self.bookCatalog.append(sb)
                self.indexKey.add(key, self.bookCatalog.size()-1)
                self.indexSortedPrefix.add(title, self.bookCatalog.size()-1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

        return self.bookCatalog.size()

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the shopping cart the book with index i
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.push(s)
            elapsed_time = time.time() - start_time
            print(s)
            '''
            print("\nThe following Book has been Added to your Shopping Cart","\n\n\tBook: ", s.key,
                      "\n\t\tTitle: ", s.title, "\n\t\tGroup: ",
                      s.group, "\n\t\tRank: ", s.rank,
                      "\n\t\tSimilar: ",s.similar ,f"\nCompleted in {elapsed_time} seconds")
            '''

    def addBookByKey(self, s : str) :
        '''
        addBookByIndex: Inserts into the shopping cart the book with key s
        input:
            s: key string
        '''
        '''
        for i in self.bookCatalog:
            if(i.key == s):
                book = i
        self.indexKey.add(s, book)
        '''
        indexB = self.indexKey.find(s)
        if indexB != None:
            self.addBookByIndex(indexB)
            #print("s: ", s, "book: ", indexB)


    def addBookByPrefix(self, s : str) :
        '''
        addBookByPrefix: Inserts into the shopping cart the book with prefix s
        input: 
            s: Prefix    
        '''
        # Validating the index. Otherwise it  crashes
        #print(s)
        indexB = self.indexSortedPrefix.find(s)
        if indexB != None:
            self.addBookByIndex(indexB)

    def pathLength(self, s1: str, s2: str) :
        i = self.indexKey.find(s1)
        j = self.indexKey.find(s2)
        distance = self.similarGraph.distance(i, j)
        print(f"{s1} and {s2} are at distance {distance}")
        return distance



    def searchBookByInfix(self, infix : str) -> int:
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string 
        returns: 
            the number of books that contains infix in its title   
        '''
        start_time = time.time()
        numberOfBooks = 0
        for temp_index in self.bookCatalog:
            if ((infix in temp_index.title)):
                # key, title, group, rank, similar
                '''
                ones = str(numberOfBooks+1)
                if(ones[len(ones)-1] == "1" and not(ones[len(ones)-2] == "1")): end = "st"
                elif (ones[len(ones)-1] == "2" and not(ones[len(ones)-2] == "1")): end = "nd"
                elif (ones[len(ones)-1] == "3" and not(ones[len(ones)-2] == "1")): end = "rd"
                else: end = "th"
                '''
                j = self.indexKey.find(infix)
                if j != None:
                    self.similarGraph.add_edge(numberOfBooks, j)
                #temp_index.rank = temp_index.rank*-1
                self.bestSeller.add(temp_index)
                numberOfBooks += 1
                if(numberOfBooks == 50):
                    break
        for i in range(0,self.bestSeller.size()):
            print(self.bestSeller.remove())
        #print(self.similarGraph)
        #for i in self.similarGraph:
         #   print("Similar: ", i)

        elapsed_time = time.time() - start_time
        print(f"Searched {numberOfBooks} books by infix in {elapsed_time} seconds")
        return numberOfBooks

    def sortUsingMergeSort(self) :
        algorithms.merge_sort(self.bookSortedCatalog)

    
    def sortUsingQuickSort(self) :
        algorithms.quick_sort(self.bookSortedCatalog)

    def searchBookUsingBinarySearch(self, prefix : str) :
        s = SortableBook.SortableBook(0, prefix, "", 0, None)
        j = algorithms.binary_search(self.bookSortedCatalog, s)
        print(self.bookSortedCatalog[j])

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.pop()
            elapsed_time = time.time() - start_time

            print("\nThe following Book has been Removed from your Shopping Cart","\n\n\tBook: ", u.key,
                      "\n\t\tTitle: ", u.title, "\n\t\tGroup: ",
                      u.group, "\n\t\tRank: ", u.rank,
                      "\n\t\tSimilar: ",u.similar ,f"\nCompleted in {elapsed_time} seconds")
            return u
        else:
            print("Shopping Cart is empty; There's nothing else to remove.")


#a = BookStore()
#a.loadCatalog("booktest.txt")
#a.sortUsingMergeSort()

#a = BookStore()
#a.loadCatalog("booktest.txt")
#a.sortUsingQuickSort()

#a.searchBookUsingBinarySearch("Patterns of Preaching: A Sermon Sampler")
#Patterns of Preaching: A Sermon Sampler
#a.searchBookUsingBinarySearch("World of Po")



#a = BookStore()
#a.loadCatalog("booktest.txt")
#a.searchBookByInfix("Patterns of ")
