from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Request
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'image', 'description']


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'phone_number', 'userinfo','item', 'message']