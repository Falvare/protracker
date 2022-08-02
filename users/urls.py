from django.urls import path
from .views import register, Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
