###H24126078鄭雅云
###統計116

def add_book(library):
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """

    details = input("Enter title, genre, and price of the book separated by a vertical bar | character: ")
    try:
        title, genre, price = details.split("|")
        title = title.strip()
        genre = genre.strip()
        price = float(price.strip())  # 轉成浮點數，不然會有Typeerror
        if title in library:
            print(f"The book '{title}' already exists in the library.")
            return False
        else:
            library[title] = {"genre": genre, "price": price}
            print(f"The book '{title}' has been added to the library.")
            return True  ###return False讓底下條件成立，接著運作下去
    except ValueError:
        print("Invalid input. Please ensure that the price is a number and the input is in the correct format.")
        return False  ###return False讓底下條件不成立



def remove_book(library):
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """

    title = input("Enter the title of the book you want to remove: ").strip()
    if title in library:
        del library[title]  ###從字典中刪除
        print(f"The book '{title}' has been removed from the library.")
        return True
    else:
        print(f"The book '{title}' is not found in the library.")
        return False



def get_book_info(library):
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    title = input("Enter the title of the book: ").strip()
    if title in library:
        book = library[title]
        print()
        print(f"Title: {title}, Genre: {book['genre']}, Price: {book['price']}")
    else:
        print(f"The book '{title}' is not found in the library.")



def list_books(library):
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """

    if library:
        print("Listing all books in the library:")
        for title in sorted(library.keys()):
            book = library[title]
            print(f"Title: {title}, Genre: {book['genre']}, Price: {book['price']:.2f}")
    else:
        print("The library is empty.")



def list_books_by_genre(library):
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """

    genre = input("Enter the genre: ").strip()  ###strip是為了讓前後空白消失
    books_in_genre = {title: info for title, info in library.items() if info["genre"] == genre}
    if books_in_genre:
        print()
        print(f"Listing all books in the genre '{genre}':")
        for title in sorted(books_in_genre.keys()):
            book = books_in_genre[title]
            print(f"Title: {title}, Price: {book['price']:.2f}")
    else:
        print(f"No books found in the genre '{genre}'.")



def list_books(library):
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:  ###如果字典中還是空的
        print("\nThe library is empty.\n")
        return False
    print()

    for title in sorted(library.keys()):
        book = library[title]
        print("%s (%s, $%.2f)" % (title, book["genre"], book["price"]))
    print()
    return True



def main():  ###主結構
    library = {}
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Get book information")
        print("4. List all books")
        print("5. List books by genre")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            if add_book(library):
                list_books(library)
        elif choice == "2":
            if remove_book(library):
                list_books(library)
        elif choice == "3":
            get_book_info(library)
        elif choice == "4":
            list_books(library)
        elif choice == "5":
            list_books_by_genre(library)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    print("Goodbye!")

if __name__ == "__main__":
    main()