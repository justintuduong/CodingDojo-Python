from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request): 
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    print(request.session['count'])
    context = {
        "unique_id": get_random_string(length=32),
        "count": request.session['count']
    }
    return render(request,"index.html", context)

def clear(request):
    request.session['count'] = 0
    return redirect("/clear")
    