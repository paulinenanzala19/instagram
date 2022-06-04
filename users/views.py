from django.shortcuts import render
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from instagram.models import *

# Create your views here.
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            LOGIN_REDIRECT_URL='instagram-index'
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f' Account for {username} has been created successfully!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/registration.html', {'form':form})
