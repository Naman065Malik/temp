from django.shortcuts import render, redirect
from Post.models import Post
from .models import Like,Love,Funny,Sad,Wow,Angry

def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.reactions
    liked = Like.objects.filter(user=user, post=post).count()

    if not liked:
        Liked = Like.objects.create(user=user, post=post)
        
        current_likes = current_likes + 1
    else:
        Liked = Like.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        
    post.reactions = current_likes
    post.save()
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    return redirect('home')

def love(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.reactions
    liked = Love.objects.filter(user=user, post=post).count()

    if not liked:
        Liked = Love.objects.create(user=user, post=post)
        
        current_likes = current_likes + 1
    else:
        Liked = Love.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        
    post.reactions = current_likes
    post.save()
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    return redirect('home')

def funny(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.reactions
    liked = Funny.objects.filter(user=user, post=post).count()

    if not liked:
        Liked = Funny.objects.create(user=user, post=post)
        
        current_likes = current_likes + 1
    else:
        Liked = Funny.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        
    post.reactions = current_likes
    post.save()
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    return redirect('home')

def sad(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.reactions
    liked = Sad.objects.filter(user=user, post=post).count()

    if not liked:
        Liked = Funny.objects.create(user=user, post=post)
        
        current_likes = current_likes + 1
    else:
        Liked = Funny.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        
    post.reactions = current_likes
    post.save()
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    return redirect('home')

def angry(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.reactions
    liked = Angry.objects.filter(user=user, post=post).count()

    if not liked:
        Liked = Funny.objects.create(user=user, post=post)
        
        current_likes = current_likes + 1
    else:
        Liked = Funny.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        
    post.reactions = current_likes
    post.save()
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    return redirect('home')

def wow(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.reactions
    liked = Wow.objects.filter(user=user, post=post).count()

    if not liked:
        Liked = Funny.objects.create(user=user, post=post)
        
        current_likes = current_likes + 1
    else:
        Liked = Funny.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        
    post.reactions = current_likes
    post.save()
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    return redirect('home')
