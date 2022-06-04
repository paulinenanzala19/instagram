from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import *


# Create your views here.
def home(request):
    posts=Post.objects.all()
    
    return render(request, 'index.html',{'posts':posts})
    
