# # Program to help Annie find her favorite book in her grandmother's library.
#
# # Input the book Annie is searching for.
# search_book = input()
#
# # Initialize a counter for the number of books checked.
# count = 0
#
# while True:
#     # Input the name of the next book in the library.
#     current_book = input()
#
#     # Check if there are no more books left in the library.
#     if current_book == "No More Books":
#         print("The book you search is not here!")
#         print(f"You checked {count} books.")
#         break
#
#     # Check if the current book is the one Annie is searching for.
#     if current_book == search_book:
#         print(f"You checked {count} books and found it.")
#         break
#
#     # Increment the counter as the book was checked and not found.
#     count += 1

searched_title = input()
title = ""
books_searched = 0

while searched_title != title:
    title = input()

    if searched_title == title:
        print(f"You checked {books_searched} books and found it.")
        break
    elif title == "No more Books":
        print("The book you search is not here!")
        print(f"You checked {books_searched} books.")
        break

    books_searched += 1