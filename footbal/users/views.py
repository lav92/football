from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


from users.forms import UserLoginForm, UserRegisterFrom, UserProfile

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


class ChangeView(UpdateView):
    form_class = UserProfile
    template_name = 'users/profile.html'
    success_url = reverse_lazy('main-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Your Profile'
        context['token'] = Token.objects.get(user_id=self.request.user.pk)
        return context

    def get_object(self, *args, **kwargs):
        return self.request.user


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main-page'))
