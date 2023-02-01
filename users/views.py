from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import CustomUserCreateForm,ProfileForm,UpdateUser
from django.contrib.auth.models import User

# Create your views here.
def profiles(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request,'users/profiles.html',context=context)


@login_required(login_url='login')
def editProfile(request):
    form = UpdateUser(instance=request.user)
    if request.method == 'POST':
        form = UpdateUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"Profile Update Successfully !!!")
        else:
            messages.error(request,"Something Wrong !!!")
            return redirect('editprofile')
    context = {"form":form}
    return render(request,'users/editprofile.html',context=context)


def signupUser(request):
    page = "signup"
    form = CustomUserCreateForm()
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"User Create Successfully !!!")
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,"Something Wrong !!!")
            return redirect('signup')
    context = {"page":page,"userForm":CustomUserCreateForm}
    return render(request,"users/signup.html",context=context)
    

def logoutUser(request):
    logout(request)
    return redirect('login')    

def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST' and page == 'login':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            User.objects.get(username=username)
        except:
            messages.error(request,'Username Not Found !!')
        
        user  = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'Username Or Password is Incorrect !!')
    context = {"page":page}
            
    return render(request,'users/login.html',context=context)

@login_required(login_url='login')
def userAccount(request):
    user = request.user
    context = {"user":user}
    return render(request,'users/user.html',context)


