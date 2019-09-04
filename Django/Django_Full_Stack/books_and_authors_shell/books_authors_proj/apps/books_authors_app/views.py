from django.shortcuts import render, HttpResponse, redirect
from .models import *


# ------------------------------------------------------------
# Index page, POST DONE
# ------------------------------------------------------------

def index(request): #POST FORM render + book show table
    # nothing needed for form (left side of html)
    context = {                                                 #context is used to retrieve data from db to display on html
        "all_books" : Book.objects.all()
    }
    # print(context)
    return render(request, "index.html", context)


# ------------------------------------------------------------
# ADD BOOKS, POST REDIRECT DONE
# ------------------------------------------------------------

def add_books(request): #POST FORM redirect
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["description"]
        add_book = Book.objects.create(title = title, desc = desc)
        # print(add_book)
    return redirect("/")

# ------------------------------------------------------------
# BOOK_DESC, DONE
# ------------------------------------------------------------

def book_desc(request, book_id):
    context = {
        "all_authors" : Author.objects.all(),
        "book" : Book.objects.get(id=book_id),
        "authors_list" : Book.objects.get(id=book_id).authors
    }
    return render(request, "book_description.html", context)

# ------------------------------------------------------------
# POST FORM, Add author on book desc. page DONE
# ------------------------------------------------------------

def add_author_to_book(request):
    if request.method == "POST":
        author_id = request.POST["author_id"]
        book_id = request.POST["book_id"]
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=author_id)
    add_author_to_book = this_book.authors.add(this_author)
    # print(str(book_id))
    return redirect("/book_desc/"+ str(book_id))











# ------------------------------------------------------------
# AUTHORS, POST REDIRECT DONE
# ------------------------------------------------------------

def authors(request): #POST FORM
    context = {
        "all_authors" : Author.objects.all()
    }
    return render(request, "authors.html", context)


# ------------------------------------------------------------
# Add new author DONE
# ------------------------------------------------------------

def add_new_author(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        notes = request.POST["notes"]
    add_author = Author.objects.create(first_name = first_name, last_name = last_name, note=notes)
    # print(add_book)
    return redirect("/authors")


# ------------------------------------------------------------
# AUTHOR NOTES DONE
# ------------------------------------------------------------

def author_notes(request, author_id):
    context = {
        "all_books" : Book.objects.all(),
        "author" : Author.objects.get(id=author_id),
        "books_list" : Author.objects.get(id=author_id).books
    }
    return render(request, "author_notes.html", context)


# ------------------------------------------------------------
# POST FORM, Add author on book desc. page NEED TO CHANGE CODE
# ------------------------------------------------------------

def add_book_to_author(request):  
    if request.method == "POST":
        author_id = request.POST["author_id"]
        book_id = request.POST["book_id"]
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=author_id)
    add_books_to_author = this_author.books.add(this_book)
    # print(str(book_id))
    return redirect("/author_notes/"+ str(author_id))

