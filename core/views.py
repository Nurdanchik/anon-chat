from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post, Request
from .forms import SignUpForm,PostForm, RequestForm

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

@login_required
def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'core/frontpage.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()
            return redirect('frontpage')
    else:
        form = PostForm()
    
    return render(request, 'core/create_post.html', {'form': form})


@login_required
def requestpage(request):
    filled_requests = Request.objects.all()
    return render(request, 'core/requestpage.html', {'filled_requests': filled_requests})


@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)

        if form.is_valid():
            post = form.save()
            return redirect('frontpage')
    else:
        form = RequestForm()
    
    return render(request, 'core/buy.html', {'form': form})