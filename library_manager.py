# Description: A simple library management system that allows users to add, remove, search, and display books in a library.

import json
import os

# File to store the library data

LIBRARY_FILE = "library.txt"

def load_library():
    """🔎 Load the library from a library.txt file."""
    if os.path.exists(LIBRARY_FILE):
        try:
            with open(LIBRARY_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_library(library):
    """Save the library to a library.txt file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Load existing library data

library = load_library()

def add_book():
    """Add a new book to the library."""
    title = input("✅ Enter the book title 📖 : ").strip()
    author = input("✅ Enter the author 📔 : ").strip()
    year = input("✅ Enter the publication year 📗 : ").strip()
    genre = input("✅ Enter the genre 📕 : ").strip()
    read_status = input("🔔 Have you read this book? (yes/no) 📗 : ").strip().lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status,
    }

    library.append(new_book)
    save_library(library)
    print(f"\n✅ '{title}' by {author} added successfully🤗!\n")

def remove_book():
    """Remove a book from the library by title."""
    title = input("✅ Enter the title of the book to remove: ").strip()
    global library
    updated_library = [book for book in library if book["title"].lower() != title.lower()]

    if len(updated_library) < len(library):
        library = updated_library
        save_library(library)
        print(f"\n✅ '{title}' removed successfully!\n")
    else:
        print("\n⚠️ Book not found in the library.\n")

def search_books():
    """🔎 Search for a book by title or author."""
    search_query = input("\n\t 📖 Enter title or author to search 📚 : ").strip().lower()
    results = [book for book in library if search_query in book["title"].lower() or search_query in book["author"].lower()]

    if results:
        print("\n📖 Matching Books:")
        for book in results:
            print(f"🔹 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '📌 Unread'}")
    else:
        print("\n⚠️ No matching books found.")

def display_books():
    """📚 Display all books in the library."""
    if not library:
        print("\n📌 Your library is empty. Add some books first!📦 \n")
        return

    print("\n📚 Your Library Collection:")
    for index, book in enumerate(library, start=1):
        print(f"{index}. 📖 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '📌 Unread'}")

def display_statistics():
    """Display statistics about the library."""
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print("\n📊 Library Statistics:")
    print(f"📚 Total Books: {total_books}")
    print(f"📖 Books Read: {read_books} ({percentage_read:.2f}%)")

  
def main():
    """Main function to run the menu-driven program."""
    while True:
        print("\n\t📖 Welcome to the Library Management System 📘")
        print("\n :Menu:")
        print("\n1️⃣   Add a book")
        print("2️⃣   Remove a Book")
        print("3️⃣   Search for a Book")
        print("4️⃣   Display All Books")
        print("5️⃣   View Statistics")
        print("6️   Exit")

        choice = input("\n🧧 Enter your choice:").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("\n📂📚 Thank you for using the Library System! Goodbye 👋😇\n")
            break
        else:
            print("\n❌Invalid choice. Please try again🔎!!!!\n")

if __name__ == "__main__":
    main()

# End of the program