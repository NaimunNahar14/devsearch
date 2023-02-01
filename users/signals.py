from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

def profileUpdate(sender,instance,created, **kwargs):
    if(created):
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )


def update(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.firstname = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()



post_save.connect(update,sender=User)
post_save.connect(profileUpdate,sender=User)