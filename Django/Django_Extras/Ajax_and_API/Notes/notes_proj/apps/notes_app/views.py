from django.shortcuts import render, HttpResponse
def index(request):
    return render (request, "notes_app/notes.html")