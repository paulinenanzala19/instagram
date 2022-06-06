from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from insta.models import *

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f' Account for {username} has been created successfully!')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'django_registration/registration_form.html', {'form':form})

def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  prof_form.is_valid():
            user_form.save()
            prof_form.save()

            return redirect('profile')

    else:
        
        prof_form = ProfileUpdateForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        context = {
            'user_form':user_form,
            'prof_form': prof_form
        }

        return render(request, 'profile/profile.html', context)