from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Post
from .forms import SignUpForm,PostForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'core/frontpage.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()
            return redirect('frontpage')
    else:
        form = PostForm()
    
    return render(request, 'core/create_post.html', {'form': form})