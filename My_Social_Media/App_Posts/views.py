from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from App_Login.models import User_Profile_Model, Follow_Model
from App_Posts.models import Post_Model, Like_Model
# Create your views here.

@login_required
def Home_View(request):
    diction = {}
    if request.method == 'GET':
        search = request.GET.get('search', '')
        results = User.objects.filter(username__icontains=search)
        diction.update({'search' : search})
        diction.update({'results' : results})

    following_list = Follow_Model.objects.filter(follower=request.user)
    posts = Post_Model.objects.filter(author__in = following_list.values_list('following'))
    diction.update({'title' : 'Homepage'})
    diction.update({'following_list' : following_list})
    diction.update({'posts' : posts})

    liked_posts = Like_Model.objects.filter(liker = request.user)
    liked_posts_list = liked_posts.values_list('post', flat=True)
    print(liked_posts_list)
    diction.update({'liked_posts_list' : liked_posts_list})
    return render(request, 'App_Posts/home_page.html', context=diction)


def Like_View(request, pk):
    post = Post_Model.objects.get(pk=pk)
    # liked_posts = Like_Model.objects.filter()
    already_liked = Like_Model.objects.filter(post=post, liker=request.user)
    if not already_liked:
        obj = Like_Model(post = post, liker = request.user)
        obj.save()
    return HttpResponseRedirect(reverse('home'))


@login_required
def Unlike_View(request, pk):
    already_liked = Like_Model.objects.filter(post = Post_Model.objects.get(pk=pk), liker = request.user)
    if already_liked:
        already_liked.delete()
    return HttpResponseRedirect(reverse('home'))
