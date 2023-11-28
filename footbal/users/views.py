from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserLoginForm, UserRegisterFrom

# Create your views here.


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Authorization',
    }


class RegisterUser(CreateView):
    form_class = UserRegisterFrom
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Register',
    }
    success_url = reverse_lazy('users:login')
