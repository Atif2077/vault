from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    pass

class Chats(models.Model):
    user = models.CharField("username", default="user1", max_length=64)
    data = models.CharField("chat", blank=False, max_length=64)
    to_user = models.CharField("user", default="user", max_length=24)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} has send message to {self.to_user}"
    
class Person(models.Model):
    user = models.CharField("username", default="user1", max_length=64)
    edit_able = models.BooleanField(default=False)
    time = models.DateTimeField(("last updated"),auto_now_add=True)
    def __str__(self):
        return f"id of {self.user}"
    
class Books(models.Model):
    user = models.CharField("username", default="user1", max_length=64)
    title = models.CharField("Title", default="Book", max_length=64)
    link = models.CharField("Book link", default="/chat/index.html", max_length=1024)
    image = models.CharField("Book image link",max_length=1024 ,default="https://static.vecteezy.com/system/resources/previews/009/399/398/non_2x/old-vintage-book-clipart-design-illustration-free-png.png")
    author = models.CharField("Book link", max_length=1024)
    time = models.DateTimeField(("Last Update"),auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} was last updated on {self.time} by {self.user}" 
    
    
class Assignment(models.Model):
    user = models.CharField("username", default="user1", max_length=64)
    name = models.CharField("assignment", default="assignment", max_length=256)
    prof = models.CharField("username", default="user1", max_length=64)
    time = models.DateField("deadline")
    def __str__(self):
        return f"{self.prof} has given this to be completed on {self.time}"
    
class Notes(models.Model):
    user = models.CharField("username", default="user1", max_length=64)
    subject_name = models.CharField("subject_name", default="biotech", max_length=256)
    student = models.CharField("name", default="user1", max_length=64)
    time = models.DateTimeField("updated on:", auto_now_add=True)
    description = models.TextField("description")
    link = models.URLField("url for the notes")
    def __str__(self):
        return f"{self.user} has given this notes of {self.student}"