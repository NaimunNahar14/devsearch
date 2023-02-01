from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

from django.db.models.signals import post_save


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    demo_link = models.URLField(max_length=200)
    project_img = models.ImageField(null=True,blank=True,default='default.jpg')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True, default=User)
    vote_ration = models.DecimalField(max_digits=2, decimal_places=1)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField('Tag',blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True, editable=False)


    def __str__(self):
        return self.name



def profileUpdate(sender,instance,created, **kwargs):
    print("Profile Updated !!")


post_save.connect(profileUpdate,sender=Project)

