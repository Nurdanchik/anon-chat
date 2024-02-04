from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_request/', views.create_request, name='create_request'),
    path('requestpage/', views.requestpage, name='requestpage'),
]