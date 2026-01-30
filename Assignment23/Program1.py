"""1. Write a Python program to implement a class named BookStore with the following specifications:
The class should contain two instance variables:
Name (Book Name)
Author (Book Author)
The class should contain one class variable:
NoOfBooks (initialize it to 0)
Define a constructor (__init__) that accepts Name and Author and initializes instance variables.
Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
Implement instance method:
Display() - should display book details in the format:
<BookName> by <Author>. No of books: <NoOfBooks>"""

class BookStore:
    No_Of_Books = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.No_Of_Books += 1 # increment when object is created

    def Display(self):
        print(self.Name, "by", self.Author, ". No of books:", BookStore.No_Of_Books)

# Creating objects
B1 = BookStore("Linux System Programming", "Robert Love")
B1.Display()

B2 = BookStore("C Programming", "Dennis Ritchie")
B2.Display()
