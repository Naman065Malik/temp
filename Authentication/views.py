from django.shortcuts import render, redirect
from .models import User
from django.urls import resolve
from django.shortcuts import render, redirect, get_object_or_404
from Post.models import Post, Follow, Stream, Favourite
from django.core.paginator import Paginator


# Create your views here.
def register(request):
    if request.method == "POST":
        user = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Pass = request.POST["pass"]
        privacy_check = request.POST.get('privacy', False)

        if privacy_check:


            if password == Pass:
                New = User.objects.create(email=email,username=user,password=password)

                New.save()

                return redirect('home')

            context = {'message':'Please Enter Same Password','flag':True}
            return render(request,'register.html',context=context)

        context = {'message':'Please acceept the privacy','flag':True}
        return render(request,'register.html', context=context)

    context = {'message':'','flag':False}
    return render(request,"register.html",context=context) 

 
def userProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = User.objects.get(username=user)
    profiles = User.objects.all()
    url_name = resolve(request.path).url_name
    posts = Post.objects.filter(user=user).order_by('-posted')
    favo = Favourite.objects.get(user=user)
    fav = favo.favourite.all()
    # if url_name == 'profile':
    #     posts = Post.objects.filter(user=user).order_by('-posted')
    # else:
    #     posts = user.profile.favourite.all()
        
    # Profile Stats
    

    
    # pagination
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    context = {    
        'profile':profile,
        'posts': posts,
       
        'posts_paginator':posts_paginator,
        'favourite':fav,
        
        
        
    }
    return render(request, 'profile.html', context)    

