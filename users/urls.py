from django.urls import path
from .views import profiles,loginPage,logoutUser,signupUser,userAccount,editProfile

urlpatterns = [

    path('login',loginPage,name='login'),
    path('logout',logoutUser,name='logout'),
    path('signup',signupUser,name='signupuser'),
    path('user',userAccount,name='user'),
    path('edit-profile',editProfile,name='editprofile'),
    path('',profiles,name='profiles'),

]
