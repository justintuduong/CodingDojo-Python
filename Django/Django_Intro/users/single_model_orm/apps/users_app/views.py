from django.shortcuts import render, HttpResponse
from.models import users

def index(request):
    context = {
        "all_users": users.objects.all()
    }
    return render(request, "users_app/index.html",context)