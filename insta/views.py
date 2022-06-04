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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'caption', 'image']
    template_name = 'instagram/post.html'

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