from . import views
from django.urls import path,include
from django.conf import settings
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views


urlpatterns=[
    path('',views.home, name='home'),
    path('<int:pk>',views.likes, name='likes'),
    
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)