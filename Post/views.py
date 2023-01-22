from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponseRedirect, HttpResponse
from Post.models import Tag, Stream, Follow, Post, Likes, Favourite
from django.contrib.auth.decorators import login_required
from Authentication.models import User
# Create your views here.
from Post.forms import NewPostform
from django.urls import reverse
# from user.models import Profile



def index(request):

    user = request.user
    posts = Stream.objects.filter(user=user) 
    group_ids =[]

    for post in posts:
        group_ids.append(post.post_id)
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    context = {
        'post_items' : post_items,
    }
    
    return render(request, 'index.html', context)

def NewPost(request):
    user = request.user
    # profile = get_object_or_404(Profile, user=user)
    tags_obj = []
    
    if request.method == "POST":
        form = NewPostform(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tags')
            tag_list = list(tag_form.split(','))

            for tag in tag_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_obj.append(t)
            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user=user)
            p.tags.set(tags_obj)
            p.save()
            return redirect(index)
    else:
        form = NewPostform()
    context = {
        'form': form
    }
    return render(request, 'newpost.html', context)




def PostDetails(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    context ={
        'post': post,
    }
    

    return render(request, 'post-details.html', context)

# nOT REQUIRED NEW OPTION IS MADE IN REACTIONS APP
# @login_required
# def like(request, post_id):
#     user = request.user
#     post = Post.objects.get(id=post_id)
#     current_likes = post.likes
#     liked = Likes.objects.filter(user=user, post=post).count()

#     if not liked:
#         Liked = Likes.objects.create(user=user, post=post)
        
#         current_likes = current_likes + 1
#     else:
#         Liked = Likes.objects.filter(user=user, post=post).delete()
#         current_likes = current_likes - 1
        
#     post.likes = current_likes
#     post.save()
#     # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
#     return HttpResponseRedirect(reverse('post-details', args=[post_id]))

# Not Required New option is made below (save)
# def favourite(request, post_id):
#     user = request.user
#     post = Post.objects.get(id=post_id)
#     fav = Favourite.objects.get(user = user)
    
#     if fav.favourite.filter(id=post_id).exists():
#         fav.favourite.remove(post)
#     else:
#         fav.favourite.add(post)
#     return HttpResponseRedirect(reverse('post-details', args=[post_id]))

@login_required
@csrf_exempt
def save(request):
    user = request.user
    # id = request.POST['Post_id']
    data = json.loads(request.body)
    id = data['Post_id']
    post = Post.objects.get(id=id)
    fav = Favourite.objects.get(user = user)
    if fav.favourite.filter(id=id).exists():
        fav.favourite.remove(post)
    else:
        fav.favourite.add(post)
    return HttpResponse()
    
    
    
