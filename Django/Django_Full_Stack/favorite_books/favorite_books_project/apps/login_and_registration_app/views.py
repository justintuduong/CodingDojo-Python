from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from datetime import datetime
from django.contrib import messages
import bcrypt


def index(request):
    if request.session['active'] == False:
        return redirect('/')

    user_id = request.session['id']
    context = {
        "user" : User.objects.get(id=user_id)
    }
    print(user_id)
    return render(request, "favorite_books_app/home_page.html", context)





