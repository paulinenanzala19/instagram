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

# def post(request, pk):
#     post = Post.objects.get(pk=pk)
#     user = request.user
#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 author= user,
#                 content=form.cleaned_data["content"],
#                 post=post
#             )
#             comment.save()

#     comments = Comment.objects.filter(post=post).order_by('-date_posted')
#     context = {
#         "post": post,
#         "comments": comments,
#         "form": form,
#     }

#     return self.get(self, request, pk, context)

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