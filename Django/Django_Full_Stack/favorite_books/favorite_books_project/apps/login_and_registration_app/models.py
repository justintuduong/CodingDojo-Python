from django.db import models
from apps.favorite_books_app.models import *
import re
import bcrypt 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        # if User.objects.values(request.POST['email']).annotate(Count("id"))
        # if User.objects.filter(email = postData['email']) > 0:
        #     errors["email"] = "Email already exists"
        if not EMAIL_REGEX.match(postData["email"]) :
            errors["email"] = "Invalid email address"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must have at least 8 characters"
        if postData["password"] != postData["password_confirm"]:
            errors["password_confirm"] = "Password does not match"
        return errors

    def log_validator(self, postData):
        errors = {}
        user_credentials = User.objects.filter(email=postData["email"])
        if len(user_credentials) < 1:
            errors["login_credentials"] = "Invalid login credentials "
        # if User.objects.filter(email = postData['email']) < 1:
        #     errors["email"] = "Email does not exist"
        for email in user_credentials:
            if not bcrypt.checkpw(postData["password"].encode(), email.password.encode()):
                errors["login_credentials"] = "Invalid login credentials"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
