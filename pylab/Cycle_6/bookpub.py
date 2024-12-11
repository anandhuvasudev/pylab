# Base class Publisher
class Publisher:
    def __init__(self, publisher_id, publisher_name):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name

    def display_info(self):
        print(f"Publisher ID: {self.publisher_id}")
        print(f"Publisher Name: {self.publisher_name}")


# Derived class Book
class Book(Publisher):
    def __init__(self, publisher_id, publisher_name, title, author):
        super().__init__(publisher_id, publisher_name)  # Invoke base class constructor
        self.title = title
        self.author = author

    def display_info(self):
        super().display_info()  # Call base class method
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


# Derived class Python
class Python(Book):
    def __init__(self, publisher_id, publisher_name, title, author, price, no_of_pages):
        super().__init__(publisher_id, publisher_name, title, author)  # Invoke parent class constructor
        self.price = price
        self.no_of_pages = no_of_pages

    def display_info(self):
        super().display_info()  # Call parent class method
        print(f"Price: ${self.price}")
        print(f"Number of Pages: {self.no_of_pages}")


# Main Program
def main():
    print("Enter details of the Python book:")
    publisher_id = input("Enter Publisher ID: ")
    publisher_name = input("Enter Publisher Name: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    price = float(input("Enter Price: "))
    no_of_pages = int(input("Enter Number of Pages: "))

    # Create an instance of Python class
    python_book = Python(
        publisher_id=publisher_id,
        publisher_name=publisher_name,
        title=title,
        author=author,
        price=price,
        no_of_pages=no_of_pages,
    )

    # Display information about the Python book
    print("\nBook Details:")
    python_book.display_info()


# Run the main program
if __name__ == "__main__":
    main()
