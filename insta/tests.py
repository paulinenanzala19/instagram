from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class TestUser(TestCase):
    def setUp(self):
        self.test = User(username='test1',email='test@gmail.com',password='1234')
        self.test.save()
    def test_user_instance(self):
        self.assertTrue(isinstance(self.test,User))

class TestProfile(TestCase):
    def setUp(self):
        self.test = User(username='test1',email='test@gmail.com',password='1234')
        self.test.save()
        self.e_profile = Profile(user=self.test,image = "../uploads/img.png",bio="geri inengi")

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.e_profile,Profile))

class TestPost(TestCase):
    def setUp(self):
        self.e_profile =  Profile( user=User(username='test1'))
        # self.e_profile.save()
        self.e_post = Post(image = "../uploads/img.png",title = "yolo",caption="eat life with a big spoon",likes = 5,pub_date= "June 5, 2022, 12:19 p.m.")
    
    def tearDown(self):
        Profile.objects.all().delete()
        Post.objects.all().delete()
    
    def test_post_instance(self):
        self.assertTrue(isinstance(self.e_post,Post))

class TestComment(TestCase):
    def setUp(self):
        self.test = User(username='test1',email='test@gmail.com',password='1234')
        self.test.save()
        self.e_profile = Profile(image = "../uploads/img.png",user=User(username='test1'),bio="geri inengi")
        # self.e_profile.save()
        self.e_post = Post(image = "../uploads/img.png",title = "yolo",caption="eat life with a big spoon",user=User(username='test1'),likes = 5,pub_date= "2022-06-04 12:19")
        # self.e_post.save()
        self.e_comment = Comment(comment =self.e_profile, date ="2022-06-04 12:19",post = self.e_post)
    
    def tearDown(self):
        Profile.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()
    
    def test_comment_instance(self):
        self.assertTrue(isinstance(self.e_comment, Comment))
