class Library:
    def __init__(self, list, name):
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library:
{self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lendder-Book database has been update . You can take the book now")

        else:
            print("f"Book is alread being used by)
{self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__== 'main__':

    books = Library(['Python', 'Rick Dad poor Dad', 'Harry potter', 'C++ Basics', 'Algorithon by CLRS'], "Let's Upskill")

    while(Ture):
        print(f"Welcome to the {book.name} library. Enter your choice to continue")
        print("1. Display Books")          
        print("2. Lend a Books")     
        print("3. Add a Books") 
        print("4. Return a Books") 
        user_choice = input ()
        if user_choice not in ['1', '2', '3', '4']:
           print("Please enter a valid option")
           continue
        
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
           books.displayBooks()

        elif user_choice == 2:
            books = input("Enter the name of the book you want to lend:")

lend:")
        elif user_cho            