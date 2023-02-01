from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    short_intro = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    profile_img = models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/profile.jpg')
     
    def __str__(self):
        return self.username
    

