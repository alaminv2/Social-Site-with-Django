from django.shortcuts import render, HttpResponseRedirect
from .forms import Sign_Up_Form, Edit_Profile_Form
from .models import User_Profile_Model, Follow_Model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Posts.forms import Post_Form
from django.contrib.auth.models import User


# Create your views here.

def Sign_Up_View(request):
    diction = {}
    registered = False
    form = Sign_Up_Form()
    if request.method == 'POST':
        form = Sign_Up_Form(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            obj = User_Profile_Model(user = user)
            obj.save()
            return HttpResponseRedirect(reverse('App_Login:login'))

    diction.update({"form" : form})
    diction.update({"title" : '"Sign Up"'})
    return render(request, 'App_Login/sign_up_page.html', context=diction)


def Login_View(request):
    logged_in = False
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                logged_in = True
                return HttpResponseRedirect(reverse('home'))
    return render(request, 'App_Login/login_page.html', context={'title':'Login', 'form':form, 'logged_in' : logged_in})


@login_required
def Edit_Profile_View(request):
    current_user = User_Profile_Model.objects.get(user=request.user)
    form = Edit_Profile_Form(instance=current_user)
    if request.method == 'POST':
        form = Edit_Profile_Form(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
    return render(request, 'App_Login/edit_profile_page.html', context={'title' : 'Profile', 'form' : form})


@login_required
def Logout_View(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Posts:home'))


@login_required
def User_Profile_View(request):
    form = Post_Form()
    if request.method == 'POST':
        form = Post_Form(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return HttpResponseRedirect(reverse('App_Login:user_profile'))
    return render(request, 'App_Login/user_profile_page.html', context={'title' : 'User Profile', 'form':form})


@login_required
def Other_User_View(request, username):
    user_other = User.objects.get(username=username)
    already_followed = Follow_Model.objects.filter(follower = request.user, following=user_other)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('App_Login:user_profile'))

    return render(request, 'App_Login/other_user_page.html', context={'user_other' : user_other, 'already_followed' : already_followed})


@login_required
def Follow_View(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow_Model.objects.filter(follower = follower_user, following = following_user)
    if not already_followed:
        obj = Follow_Model(follower = follower_user, following = following_user)
        obj.save()
    return HttpResponseRedirect(reverse('App_Login:other_user', kwargs={'username' : username}))


@login_required
def Unfollow_View(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow_Model.objects.filter(follower = follower_user, following = following_user)
    if already_followed:
        already_followed.delete()
    return HttpResponseRedirect(reverse('App_Login:other_user', kwargs={'username':username}))
