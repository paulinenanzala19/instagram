from . import views
from django.urls import path
from django.conf import settings
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # path('',PostListView.as_view(), name='home'),
    path('',views.home, name='home'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)