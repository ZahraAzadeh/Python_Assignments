class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Book: {self.title} | Author: {self.author} | Year: {self.year}"

# 🧑‍💻 Get book details from user
title = input("Enter the book title: ")
author = input("Enter the author's name: ")

try:
    year = int(input("Enter the publication year: "))
    book = Book(title, author, year)
    print(book.get_info())
except ValueError:
    print("Error: Please enter a valid year as a number.")
