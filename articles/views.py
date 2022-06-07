from django.shortcuts import render
from . import models


def articles_list(request):
    articles= models.Articles.objects.all().order_by("date")
    args={"articles":articles}
    return render(request,"articles/articleslist.html",args)
