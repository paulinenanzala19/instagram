from . import views
from django.urls import path
from django.conf import settings

urlpatterns=[
    path('',views.home, name='home'),
    
]