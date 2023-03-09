from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        


class UpdateUser(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
