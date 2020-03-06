# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    return render(request,"articles/article_list.html")
def article_home(request):
    articles = Article.objects.all().order_by('date')
    return render(request,"articles/article_home.html",{'articles':articles})
