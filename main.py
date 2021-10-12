import Calculator
import BookStore
import time

def menu_calculator() :
    calculator =  Calculator.Calculator()
    option=""
    while option != '0':
        print ("""
        1 Check mathematical expression 
        2 Add variable  
        3 Print expanded expression
        4 Evaluate expression
        0 Return to main menu
        """)
        option=input() 
        if option=="1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression) :
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")

        elif option=="2":
            key = str(input("Introduce the variable name: "))
            value = float(input("Introduce the value: "))
            calculator.set_variable(key, value)
           
        elif option=="3":
            expression = input("Introduce the mathematical expression: ")
            print(calculator.print_expression(expression))

        elif option=="4":
            expression = input("Introduce the mathematical expression: ")
            print(calculator.evaluate(expression))

        ''' 
        Add the menu options when needed
        '''

def menu_bookstore_system() :
    bookStore = BookStore.BookStore()
    option=""
    while option != '0':
        print("""
        1 Load book catalog
        2 Add a book to shopping cart by index 
        3 Add a book to shopping cart by key
        4 Add a book to shopping cart by prefix
        5 Search by infix
        6 Sort using MergeSort
        7 Sort using QuickSort
        8 Search by Prefix
        9 Remove from the shopping cart
        10 Degree of separation
        0 Return to main menu
        """)
        option=input() 
        if option=="1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)      
        elif option=="2":
            title = str(input("Introduce the index to add to shopping cart (You can add multiple indexes using commas Ex: 2, 5, 8) : "))
            if("," in title):
                start_time = time.time()
                books = 0
                title = title + ","
                temp = ''
                for i in range(0, len(title)):
                    if(title[i].isdigit()):
                        temp = temp + title[i]
                    elif(title[i] == ","):
                        try:
                            index = int(temp)
                            bookStore.addBookByIndex(index)
                            books += 1
                            temp = ''
                        except: print("Syntax is off")
                elapsed_time = time.time() - start_time
                print(f"\nAll {books} books have been added to your shopping cart in {elapsed_time} seconds.")
            else:
                title = int(title)
                bookStore.addBookByIndex(title)
        elif option=="3":
            title = input("Introduce the key to add to shopping cart: ")
            bookStore.addBookByKey(title)
        elif option=="4":
            title = input("Introduce the prefix to add to shopping cart: ")
            bookStore.addBookByPrefix(title)
        elif option=="5":
            title = input("Introduce the infix: ")
            bookStore.searchBookByInfix(title)
        elif option=="6":
            bookStore.sortUsingMergeSort()
        elif option=="7":
            bookStore.sortUsingQuickSort()
        elif option=="8":
            s = input("Introduce the prefix:")
            bookStore.searchBookUsingBinarySearch(s)
        elif option=="9":
            s = str(input("Would you like to remove all indexes from your shopping cart? Y|N : "))
            if(s == "Y" or "y"):
                start_time = time.time()
                temp = bookStore.shoppingCart.size()
                for i in range (0, temp):
                    bookStore.removeFromShoppingCart()
                elapsed_time = time.time() - start_time
                print(f"\nAll {temp} books have been removed from your shopping cart in {elapsed_time} seconds.")
            else:
                bookStore.removeFromShoppingCart()
        elif option=="10":
            s1 = input("Introduce the key of first book:")
            s2 = input("Introduce the key of second book:")
            bookStore.pathLength(s1, s2)
        
        
        ''' 
        Add the menu options when needed
        '''

#main: Create the main menu
def main() :
    option=""
    while option != '0':
        print ("""
        1 Calculator
        2 Bookstore System
        0 Exit/Quit
        """)
        option=input() 
        
        if option=="1":
            menu_calculator()
        elif option=="2":
            menu_bookstore_system()    

if __name__ == "__main__":
  main()
