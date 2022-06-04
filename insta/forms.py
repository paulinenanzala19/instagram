from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class UpdateForm(forms.ModelForm):
    """
    class that handles forms

    """

    class Meta:
        model=Post
        
        fields=['image','caption']
        exclude=['likes','pub_date','comments','user']