from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class BookManager(models.Manager):
    def basic_validator_add(self, postData):
        errors = {}
        
        
        
        if not len(postData['form_add_description']) > 5 :
            errors['desc'] = "Description should be more than 5 characters"
        
        if not len(postData['form_add_title']) > 1:
            errors['title'] = "Title should be at least 1 characters"
        
        return errors
    
    def basic_validator_edit(self, postData):
        errors = {}
        if len(postData['form_edit_title']) < 1:
            errors['title'] = "Title should be at least 1 characters"
        if len(postData['form_edit_description']) < 5 :
            errors['desc'] = "Description should be more than 5 characters"
        
        return errors

class Book(models.Model):
    DBtitle = models.CharField(max_length = 255)
    DBdesc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded")
    users_who_like = models.ManyToManyField(User, related_name = "liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    def __repr__(self):
        return f"<User object: {self.DBtitle} {self.DBdesc} ({self.id})>"
