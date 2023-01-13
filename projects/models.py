from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name



class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    demo_link = models.URLField(max_length=200)
    project_img = models.ImageField(null=True,blank=True,default='default.jpg')
    owner = models.ForeignKey('User',on_delete=models.CASCADE,null=True, default=User)
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




