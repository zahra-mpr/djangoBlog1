from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse("Hi! this is my about page")
    return render(request,"about.html")

def home(request):
    # return  HttpResponse("Hi! this is my homepage")
    return render(request,"home.html")