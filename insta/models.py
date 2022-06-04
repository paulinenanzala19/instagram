from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to = 'images/', default='no image')
    title = models.CharField(max_length=100, default='SOME STRING')
    caption = models.TextField(max_length=300, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    likes=models.IntegerField(null=True, default=0)
    pub_date = models.DateTimeField(default=timezone.now)