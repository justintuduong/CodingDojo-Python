from django.shortcuts import render, redirect
import datetime
import random


def index(request): # set session data here
    if not 'gold' in request.session:
        request.session['gold'] = 0
        print(request.session['gold'])
    return render(request,"ninja_gold_app/index.html")





# def farm(request):
#     return redirect(request,"ninja_gold_app/index.html")

# def farm(request):
#     return redirect(request)   
# route cave
# route house
# route casino




# this page renders and redirects app