from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('',views.index),
    path('register',views.registerview, name='register'),
    path('login/',views.login, name='login'),
    path('login',LoginView.as_view(template_name='login.html'),name='login'),
    path('/submit',views.submit, name='submit')

    
]


