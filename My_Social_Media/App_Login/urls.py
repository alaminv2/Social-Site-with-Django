from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('sign_up/', views.Sign_Up_View, name="sign_up"),
    path('login/', views.Login_View, name="login"),
    path('edit_profile/', views.Edit_Profile_View, name="edit_profile"),
    path('logout/', views.Logout_View, name="logout"),
    path('user_profile/', views.User_Profile_View, name="user_profile"),
    path('other_user/<username>/', views.Other_User_View, name="other_user"),
    path('follow/<username>/', views.Follow_View, name="follow"),
    path('unfollow/<username>/', views.Unfollow_View, name='unfollow'),
]
