from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to = 'images/', default='no image')
    title = models.CharField(max_length=100, default='SOME STRING')
    caption = models.TextField(max_length=300, null=True)