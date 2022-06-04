from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import *

# Create your models here.
class Post(models.Model):
    image=models.ImageField(upload_to = 'images/', default='no image')
    title = models.CharField(max_length=100, default='SOME STRING')
    caption = models.TextField(max_length=300, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    likes=models.IntegerField(null=True, default=0)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'