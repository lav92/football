from django.urls import path

from users.views import LoginUser, RegisterUser, ChangeView, logout_user

app_name = 'users'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='logup'),
    path('profile/', ChangeView.as_view(), name='profile'),
    path('logout/', logout_user, name='logout'),
]
