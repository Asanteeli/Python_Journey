"""
Author: Elijah Asante
Purpose: Open text doc, read and print it's content
"""

# Open up the file
with open("books.txt") as book_file:

# Read through line by line
    for book in book_file:

# Strip off leading and trailing white spaces
        open_book = book.strip()

# Display each book to the screen
        print(open_book)