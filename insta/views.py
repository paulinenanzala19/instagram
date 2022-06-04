from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import *


# Create your views here.
def home(request):
    context{
    'posts':Post.objects.all()
    }
    
    return render(request, 'index.html',context)

class PostView(ListView):
    model=Post
    template='index.html'
    context_obj='posts'

class DetailView(DetailView):
    model=post
    template='detail.html'
    context_obj='post'

    
