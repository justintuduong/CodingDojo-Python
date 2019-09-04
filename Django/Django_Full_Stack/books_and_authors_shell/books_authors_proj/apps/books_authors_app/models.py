from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__ (self):
        return f"Book: {self.title} ({self.id})>"
class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    note = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__ (self):
        return f"Author: {self.first_name} ({self.last_name}) ({self.id})>"

# add an author to a book
# this_book = Book.objects.get(id=)
# this_author = Author.objects.get(id=)
# this_book.Author.add(this_author)

# add a book to an author
# this_author = Author.objects.get(id=)
# this_book = Book.objects.get(id=)
# this_author.books.add(this_book)

# how to remove a book from author
# this_author = Author.objects.get(id=)
# this_book = Book.objects.get(id=)
# this_author.books.remove(this_book)
