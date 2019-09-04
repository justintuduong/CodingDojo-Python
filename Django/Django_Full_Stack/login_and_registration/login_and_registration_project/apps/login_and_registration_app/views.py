from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from datetime import datetime
from django.contrib import messages
import bcrypt



def index(request):
    return render(request, "login_and_registration_app/index.html")

def process_registration(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        print(errors)
    if len(errors) > 0:
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        new_user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=pw_hash)
        request.session['id'] = new_user.id
        print(request.session['id'])
        request.session['active'] = True
        print(f" SESSION ACTIVITY IS NOW {request.session['active']} ")
        print("successful registration")
        return redirect("/user/homepage")

def process_login(request):
    if request.method == "POST":
        errors = User.objects.log_validator(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            print(errors)
    if len(errors) > 0:
        return redirect('/')

    else:
        user = User.objects.get(email=request.POST["email"])
        request.session['id'] = user.id
        request.session['active'] = True
        print(request.session['id'])
        print(f" SESSION ACTIVITY IS NOW {request.session['active']} ")
        print("I AM WORKING!")
        return redirect("/user/homepage")

def home_page(request):
    if request.session['active'] == False:
        return redirect('/')
    print("homepage")
    user_id = request.session['id']
    context = {
        "user" : User.objects.get(id=user_id)
    }
    print(user_id)
    return render(request, "login_and_registration_app/home_page.html", context)


def logout(request):

    request.session.clear()
    request.session['active'] = False
    if "id" in request.session:
        print("YOU'LL NEVER FORGET ME BWAHAHA!")
    else:
        print("YOU FORGOT ME YOU ASSHOE!")

    return redirect('/')


