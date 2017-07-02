#-*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
from .models import FreeB

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the freeboard index.")
    posts = FreeB.objects.all().order_by('-created_date')
    return render(request, "index.html", {'posts' : posts})
