# Main Class for Library methods 
class Library:

    # Creating a constructor to intialize
    def __init__(self,list_books,user):
        self.list_books = list_books
        self.name = user
        # A empty dict to take info of lenders
        self.lendDict = {}
     
    # To display all books in library   
    def displayBooks(self):
        print("We have the following books:")
        for i in self.list_books:
            print(i)
     
    # To add book in library given by user       
    def addBooks(self,book):
        self.list_books.append(book)
        print(f"Book is added to {self.name} library")
     
    # To take book for rent   
    def lendBooks(self,book,name):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:name})
            print("Book Library is updated. You can now take the book now.")
            self.list_books.remove(book)
     
    # To return the book we had lend       
    def returnBooks(self,book):
        self.lendDict.pop(book)
        self.list_books.append(book)    
        print("Book Library is updated")

# A main function to run the program anywhere
def library_manager(Library):
    
    # Creating a instance
    Sumit = Library(["Python","C++ basics","Rich Daddy Poor Daddy","PHP basics","HTML,CSS and Java in one book"],"Sumit ki apni Library")
   
    print(f"Welcome to {Sumit.name}")

    # Main Loop until user wants to go out
    while True:
        print("Enter input to continue")
        
        print('''1.Display Books
2.Lend Books
3.Add Books
4.Return Books ''')
        # Loop to check that input is correct or not
        while True:
            user_choice1 = input("\n")
            if user_choice1 == "1":
                Sumit.displayBooks()
                break
            elif user_choice1 == "2":
                book = input("Enter the name of the book you want to lend: ")
                name = input("Enter your username: ")
                Sumit.lendBooks(book,name)
                break
            elif user_choice1 == "3":
                book = input("Enter the name of the book you want to add: ")
                Sumit.addBooks(book)   
                break
            elif user_choice1 == "4":
                book = input("Enter the name of the book you want to return: ")
                Sumit.returnBooks(book)
                break
            print("Enter a valid input to continue")

        # Loop to check that input is correct or not
        while True:
            print("Enter c to continue or q to quit:")
            user_choice2 = input("\n") 
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                break
            print("Enter a valid input:")
            
# Running program in main file only
if __name__ == "__main__":
    library_manager(Library)
