from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView,CreateView,UpdateView
from django.http  import HttpResponse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import *
from .forms import *
from dataclasses import fields
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    context = {
    'posts':Post.objects.all()
    }
    
    return render(request, 'index.html',context)

# class PostListView(ListView):
#     model=Post
#     template_name='index.html'
#     context_obj='posts'

class DetailView(DetailView):
    model=Post
    template='index.html'
    context_obj='post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'caption', 'image']
    # template_name = 'insta/post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'caption']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_function(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False

@login_required(login_url='/accounts/login/')
def create_post(request):
    current_user = request.user

    if request.method == 'POST':
        form = UpdateForm(request.POST,request.FILES)
        if form.is_valid():
            p_form = form.save(commit=False)
            p_form.user = current_user

            p_form.save()
        return redirect('home')
    else:
        form = UpdateForm()
    return render(request,'newpost.html',{"form":form})

def likes(request,pk):
    post = Post.objects.get(pk=pk)
    post.likes+=1
    post.save()
    return redirect('home')

def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"posts": searched_posts})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

